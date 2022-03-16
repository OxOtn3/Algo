from ast import List
from cmath import inf
from heapq import heappop, heappush

# 赋权有向图或者无向图 的 单源最短路径 问题

# Dijkstra算法有两种实现

# 1. 朴素Dijkstra算法（邻接矩阵）
# 适用于稠密图
# 时间O(n^2), 空间O(n^2)
def dijkstra_1(n: int, graph: List[List[int]], start: int) -> List[int]:
    dis = [float('inf')] * n
    dis[start] = 0
    visited = [False] * n

    
    return

# 2.堆优化（邻接表）
# 时间O(mlogn), 空间O(m)
def dijkstra_2(n: int, graph: List[List[tuple]], start: int) -> List[int]:
    """ 

    Args:
        n (int): 图中点个数
        graph (List[List[tuple]]): graph中每一项(a, wt)为(点, 权重)
        start (int): 起点

    Returns:
        List[int]: 
    """
    dis = [inf] * n
    dis[start] = 0
    pq = [(0, start)]
    while pq:
        d, x = heappop(pq)
        if dis[x] < d:
            # 已经有更短的到点x的路径
            continue
        for y, wt in graph[x]:
            new_d = dis[x] + wt
            if new_d < dis[y]:
                dis[y] = new_d
                heappush(pq, (new_d, y))
    return dis