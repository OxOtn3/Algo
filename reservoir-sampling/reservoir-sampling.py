# 给定一个数据流，数据流长度N很大，且N直到处理完所有数据之前都不可知，
# 如何在只遍历一遍数据（O(N)）的情况下，能够随机选取出m个不重复的数据。

# 这个场景强调了3件事：

# 数据流长度N很大且不可知，所以不能一次性存入内存。
# 时间复杂度为O(N)。
# 随机选取m个数，每个数被选中的概率为m/N。

# 算法思路大致如下：

# 1.如果接收的数据量小于m，则依次放入蓄水池。
# 2.当接收到第i个数据时，i >= m，在[0, i]范围内取以随机数d，若d的落在[0, m-1]范围内，则用接收到的第i个数据替换蓄水池中的第d个数据。
# 3.重复步骤2。

# 算法的精妙之处在于：当处理完所有的数据时，蓄水池中的每个数据都是以m/N的概率获得的。

from ast import List
import random


def reservoir_sampling(m: int, dataStream: List[int]):
    reservoir = [0] * m
    for i in range(m):
        reservoir[i] = dataStream[i]
    for i in range(m, len(dataStream)):
        # 随机获得一个[0, i]内的随机整数
        d = random.randint(0, i)
        # 如果随机整数落在[0, m-1]范围内，则替换蓄水池中的元素
        if d < m:
            reservoir[d] = dataStream[i]

# 分布式蓄水池抽样：https://www.jianshu.com/p/7a9ea6ece2af