# 快速幂 递归
# 时间复杂度：O(logn)
# 空间复杂度：O(logn)
def myPow_1(x: float, n: int) -> float:
    def quickMul(N):
        if N == 0:
            return 1.0
        y = quickMul(N // 2)
        return y * y if N % 2 == 0 else y * y * x
    
    return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)


# 快速幂 迭代
# 时间复杂度：O(logn)
# 空间复杂度：O(1)
def myPow_2(x: float, n: int) -> float:
    def quickMul(N):
        ans = 1.0
        # 贡献的初始值为 x
        x_contribute = x
        # 在对 N 进行二进制拆分的同时计算答案
        while N > 0:
            if N % 2 == 1:
                # 如果 N 二进制表示的最低位为 1，那么需要计入贡献
                ans *= x_contribute
            # 将贡献不断地平方
            x_contribute *= x_contribute
            # 舍弃 N 二进制表示的最低位，这样我们每次只要判断最低位即可
            N //= 2
        return ans
    
    return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)