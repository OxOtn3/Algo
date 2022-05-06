# 树状数组
class FenwickTree:
    def __init__(self, n = 0, nums = []):
        self.len = n
        self.tree = [0] * (n + 1)
        if nums:
            for i in range(1, n + 1):
                self.update(i, nums[i-1])
    
    # 单点更新
    # 从子节点向父节点逐层更新（根据t[x]父节点为t[x+lowbit(x)]）
    # O(logn)
    def update(self, i, delta):
        while i <= self.len:
            self.tree[i] += delta
            i += self.lowbit(i)
    
    # 查询前缀和
    # 二进制分解，依次减去lowbit值，直至为0
    # 例如对于查询6的前缀和，6的二进制为0110，可以拆分为0010+0100，即t[4]的值加上t[6]的值
    # O(logn)
    def query(self, i):
        sum = 0
        while i > 0:
            sum += self.tree[i]
            i -= self.lowbit(i)
        return sum

    def lowbit(self, x):
        return x & (-x)
