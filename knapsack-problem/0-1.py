# 0-1背包

# 有 N 件物品和一个容量是 C 的背包。每件物品有且只有一件。
# 第 i 件物品的体积是 weight[i]，价值是 val[i]。
# 求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。

# 时间复杂度：O(N * C)
# 空间复杂度：O(N * C)
def solution_1(N, C, weight, val):
    dp = [[0 for j in range(C + 1)] for i in range(N)]
    # 先处理「考虑第一件物品」的情况
    for i in range(0, C + 1):
        dp[0][i] = val[0] if i >= weight[0] else 0
    # 再处理「考虑其余物品」的情况
    for i in range(1, N):
        for j in range(C + 1):
            # 不选择当前物品
            no = dp[i-1][j]
            # 选择该物品，前提「剩余容量」大于等于「物品体积」
            yes = dp[i-1][j-weight[i]] + val[i] if j >= weight[i] else 0
            dp[i][j] = max(no, yes)
    return dp[N-1][C]

# 压缩至一维
# 时间复杂度：O(N * C)
# 空间复杂度：O(C)
def solution_2(N, C, weight, val):
    dp = [0] * (C + 1)
    for i in range(N):
        # 由于计算`dp[i][j]`的时候，依赖于`dp[i-1][j-v[i]]`。
        # 因此我们在改为「一维空间优化」时，需要确保`dp[j-v[i]]`存储的是上一行的值，
        # 即确保`dp[j-v[i]]`还没有被更新，所以遍历方向是从大到小。
        for j in range(C, weight[i], -1):
            no = dp[i-1]
            yes = dp[j-weight[i]] + val[i]
            dp[j] = max(no, yes)
    return dp[C]

# 打印路径，则维护一个path数组，倒推