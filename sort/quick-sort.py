# 快速排序

# 平均时间复杂度：O(nlogn)
# 最好时间复杂度：O(nlogn)
# 最坏时间复杂度：O(n^2)

# 空间复杂度：O(1)

# 稳定性：不稳定

# 思路

# 分治

from random import random


def quickSort(nums, frm, to):
    if frm >= to:
        return
    p = partition(nums, frm, to)
    quickSort(nums, frm, p - 1)
    quickSort(nums, p + 1, to)

def partition(nums, lo, hi):
    pivot = random.randint(lo, hi)
    nums[pivot], nums[hi] = nums[hi], nums[pivot]
    i = lo - 1
    for j in range(lo, hi):
        if nums[j] < nums[hi]:
            i += 1
            nums[j], nums[i] = nums[i], nums[j]
    i += 1
    # 此时i指向的是大于pivot的数
    # 而j指向的是小于pivot的数
    # 如果交换lo, i
    # 那么lo的位置将大于pivot
    # 所以必须交换lo, j
    # 本质原因是pivot是在左边取的，即pivot = nums[lo]，交换之后需要满足lo的值小于pivot
    # 如果pivot = nums[hi]，那么就需要最后和i交换了，即swap(nums, hi, i)
    nums[i], nums[hi] = nums[hi], nums[i]
    return i

# 打乱原数组
def shuffle(nums):
    n = len(nums)
    for i in range(n):
        # 生成一个下标，区间为 [i, n)
        # 相当于和前面的（还没遍历到的）一个随机位置的数交换
        idx = i + random.randint(0, n - i - 1)
        nums[i], nums[idx] = nums[idx], nums[i]


# 快速选择
# lc215. 数组中的第K个最大元素
# https://leetcode-cn.com/problems/kth-largest-element-in-an-array/

# 相同的partition函数
def findKthLargest(nums, k):
    lo, hi = 0, len(nums) - 1
    k = len(nums) - k
    while lo <= hi:
        p = partition(nums, lo, hi)
        if p < k:
            lo = p + 1
        elif p > k:
            hi = p - 1
        else:
            return nums[p]
    return -1