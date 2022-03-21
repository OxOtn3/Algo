# 多重背包

# 有 N 件物品和一个容量是 C 的背包。
# 第 i 件物品的体积是 weight[i]，价值是 val[i]，物品件数为cnt[i]。
# 求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。

# 时间复杂度：O(N * C * S)
# 空间复杂度：O(N * C)

def solution_1(N, C, weight, val, cnt):
    dp = [[0 for j in range(C + 1)] for i in range(N)]
    # 先处理「考虑第一件物品」的情况
    for i in range(0, C + 1):
        # 当只有一件物品的时候，在容量允许，并且不超过该物品个数的情况下，能选多少件就选多少件
        maxK = min(j // weight[0], cnt[0])
        dp[0][i] = maxK * val[0]
    # 再处理「考虑其余物品」的情况
    for i in range(1, N):
        for j in range(C + 1):
            # 不选择当前物品
            no = dp[i-1][j]
            # 选择该物品
            yes = 0
            # 选择件数
            for k in range(1, cnt[i] + 1):
                if weight[i] * k > j:
                    break
                yes = max(yes, dp[i-1][j-k*weight[i]] + k * val[i])  
            dp[i][j] = max(no, yes)
    return dp[N-1][C]

# 压缩至一维，可以优化空间，但是不能降低时间复杂度。
# 时间复杂度：O(N * C * S)
# 空间复杂度：O(C)

# 因为当我们像「完全背包」那样只保留「容量维度」，并且「从小到大」遍历容量的话，
# 我们在转移f[j]时是无法直接知道所依赖的f[j-v[i]]到底使用了多少件物品i的。

# 这个问题在「完全背包」里面无须关心，因为每件物品可以被选择无限次，而在「多重背包」则是不能忽略，否则可能会违背物品件数有限的条件。

# 因此，「多重背包」问题的「一维空间优化」并不能像「完全背包」那样使复杂度降低。
def solution_2(N, C, weight, val, cnt):
    dp = [0] * (C + 1)
    for i in range(N):
        for j in range(C, weight[i], -1):
            for k in range(0, cnt[i]):
                if j < k * weight[i]:
                    break
                dp[j] = max(dp[j], dp[j-k*weight[i]] + k * val[i])
    return dp[C]