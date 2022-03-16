# 求任意两个点之间的最短路
# 适用于任何图，不管有向无向，边权正负，但是最短路必须存在。（不能有个负环）
# 复杂度比较高

# 实现：
# 定义一个数组 f[k][x][y]，表示只允许经过结点1到k的情况下，结点x到结点y的最短路长度
# 时间O(n^3), 空间O(n^2)
def floyd(dis, n):
    for k in range(1, n + 1):
        for x in range(1, n + 1):
            for y in range(1, n + 1):
                # 第一维可以压缩
                dis[x][y] = min(dis[x][y], dis[x][k] + dis[k][y])