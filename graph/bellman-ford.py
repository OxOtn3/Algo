# Bellman-Ford 算法是一种基于松弛（relax）操作的最短路算法，
# 可以求出有负权的图的最短路，并可以对最短路不存在的情况进行判断。

# 松弛操作：对于边(u, v), dis(v) = min(dis(v), dis(u) + w(u, v))

# Bellman-Ford 算法所做的，就是不断尝试对图上每一条边进行松弛。
# 我们每进行一轮循环，就对图上所有的边都尝试进行一次松弛操作，
# 当一次循环中没有成功的松弛操作时，算法停止。

# 每次循环是O(m)的，
# 在最短路存在的情况下，由于一次松弛操作会使最短路的边数至少+1，
# 而最短路的边数最多为n-1，
# 因此整个算法最多执行n-1轮松弛操作。故总时间复杂度为O(mn)。

# 还有一种情况，如果从S点出发，抵达一个负环时，松弛操作会无休止地进行下去。
# 前面的论证中已经说明了，对于最短路存在的图，松弛操作最多只会执行n-1轮，
# 因此如果第n轮循环时仍然存在能松弛的边，说明从S点出发，能够抵达一个负环。

# 需要注意的是，以S点为源点跑 Bellman-Ford 算法时，如果没有给出存在负环的结果，只能说明从S点出发不能抵达一个负环，而不能说明图上不存在负环。

# 因此如果需要判断整个图上是否存在负环，最严谨的做法是建立一个超级源点，
# 向图上每个节点连一条权值为 0 的边，然后以超级源点为起点执行 Bellman-Ford 算法。


def bellmanford(n, start):
    e = [[(0, 0) for i in range(n)] for j in range(n)]
    dis = [63] * n
    dis[start] = 0
    for i in range(1, n + 1):
        flag = False
        for u in range(1, n + 1):
            for v, w in e[u]:
                if dis[v] > dis[u] + w:
                    flag = True
        # 没有可以松弛的边时就停止算法
        if flag == False:
            break
    # 第 n 轮循环仍然可以松弛时说明 s 点可以抵达一个负环
    return flag



# 队列优化：SPFA，Shortest Path Faster Algorithm

# 很多时候我们并不需要那么多无用的松弛操作。
# 很显然，只有上一次被松弛的结点，所连接的边，才有可能引起下一次的松弛操作。
# 那么我们用队列来维护“哪些结点可能会引起松弛操作”，就能只访问必要的边了。

def spfa(n, s):
    q = []
    e = [[(0, 0) for i in range(n)] for j in range(n)]
    dis = [63] * n; cnt = [] * n; vis = [] * n
    dis[s] = 0; vis[s] = 1
    q.append(s)
    while len(q) != 0:
        u = q[0]
        q.pop()
        vis[u] = 0
        for v, w in e[u]:
            if dis[v] > dis[u] + w:
                dis[v] = dis[u] + w
                cnt[v] = cnt[u] + 1 # 记录最短路经过的边数
                if cnt[v] >= n:
                    return False
                # 在不经过负环的情况下，最短路至多经过 n - 1 条边
                # 因此如果经过了多于 n 条边，一定说明经过了负环
                if vis[v] == True:
                    q.append(v)
                    vis[v] = True