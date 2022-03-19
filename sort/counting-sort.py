# 计数排序

# 平均时间复杂度：O(n + maxV - minV)，maxV和minV差距尽可能小
# 最好时间复杂度：O(n + maxV - minV)
# 最坏时间复杂度：O(n + maxV - minV)

# 空间复杂度：O(maxV - minV)

# 稳定性：稳定

# 思路

# 是一种O(n)的排序算法，其思路是开一个长度为 maxValue-minValue+1 的数组，
# 然后分配。扫描一遍原始数组，以当前值 - minValue 作为下标，将该下标的计数器增1。
# 收集。扫描一遍计数器数组，按顺序把值收集起来。
# 举个例子， nums=[2, 1, 3, 1, 5] , 首先扫描一遍获取最小值和最大值，
# maxValue=5 , minValue=1 ，于是开一个长度为5的计数器数组 counter ，
# 1. 分配。统计每个元素出现的频率，得到 counter=[2, 1, 1, 0, 1] ，例如 counter[0] 表示值 0+minValue=1 出现了2次。
# 2. 收集。 counter[0]=2 表示 1 出现了两次，那就向原始数组写入两个1， 
# 3. counter[1]=1 表示 2 出现了1次，那就向原始数组写入一个2，依次类推，最终原始数组变为 [1,1,2,3,5] ，排序好了。

def countingSort(arr):
    # 获取最大值和最小值，确定数组长度
    minV, maxV = min(arr), max(arr)
    bucket_len = maxV - minV + 1
    bucket = [0] * bucket_len
    
    sorted_index = 0
    arr_len = len(arr)

    for i in range(arr_len):
        if not bucket[arr[i]]:
            bucket[arr[i]] = 0
        bucket[arr[i]] += 1
    for j in range(bucket_len):
        while bucket[j] > 0:
            arr[sorted_index] = j
            sorted_index += 1
            bucket[j] -= 1
    return arr

#  计数排序本质上是一种特殊的桶排序，当桶的个数最大的时候( maxV-minV+1 )，就是计数排序。