# Algo
基于 `Python3` 整理的一些算法板子，包括：
## 图论
- `Floyd`
- `Bellman-Ford`
  - 以及 `SPFA` 优化
- `Dijkstra`
  - 朴素
  - 堆优化
- `Topological Sort`
  - BFS
  - DFS
- `Kruskal`
- `Prim`

## 前缀树
- 小写英文字母的 `Trie`

## 并查集
- `Union-Find` (find优化)

## 树状数组
- `Fenwick-Tree`

## 排序
- `Heap Sort`
- `Merge Sort`
- `Quick Sort`
  - 打乱优化 
  - 以及 `Quick Select`
- `Bucket Sort`
- `Counting Sort`
- `Radix Sort`
- `Shell's Sort`

## 二叉树
- 迭代遍历（基于栈）
  - 前序
  - 中序
  - 后序
- `Morris`

## 蓄水池抽样
- `Reservoir Sampling`
  - 分布式场景下

## 数学
- `Fast Power` 快速幂
- `Newton's Method` 牛顿迭代法求平方根
- `Sieve of Eratosthenes` 埃氏筛法求素数

## 复合数据结构
- `LFU`
- `Max Frequency Stack` 最大频率栈
  - `pop()` 操作从堆栈中弹出出现频率最高的元素
- `Randomized Set` 
  - O(1) 时间插入、删除、获取随机元素
- `SnapshotArray` 快照数组
  - snap()获取该数组的快照，并返回快照的编号
  - get(index, snap_id) - 根据指定的 snap_id 选择快照，并返回该快照指定索引 index 的值。

## 计算器
- `Calculator`
  - 加减乘除
  - 括号

## 背包问题
- `0-1`
  - 空间优化
- `Unbounded` 完全背包
  - 时间、空间优化
- `Multi-Objective` 多重背包
  - 二进制优化
  - 优先队列优化
- `Multidimensional` 多维背包