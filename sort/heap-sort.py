# 堆排序

# 初始化堆需要O(n)，调整堆需要O(nlogn)
# 平均时间复杂度：O(nlogn)
# 最好时间复杂度：O(nlogn)
# 最坏时间复杂度：O(nlogn)

# 空间复杂度：O(1)，无需额外空间

# 稳定性：不稳定

# 思路（以正序排序为例）：
# 1. 将数组构造为一个大顶堆（是一个完全二叉树，父节点值大于子节点）
# 2. 将堆顶值，即最大值，与最后一个元素交换
# 3. 数组长度 -1
# 4. 再次构造堆
# 5. 重复以上步骤，直到排序完成

# 调整堆
def shiftDown(arr, n, k):
    while 2 * k + 1 < n:
        # 从当前节点的左子节点开始, 即2 * i + 1
        j = 2 * k + 1
        if j + 1 < n and arr[j + 1] < arr[j]:
            # 存在右子节点，且左子节点小于右子节点，k指向右子节点（即，先指向大的子节点）
            j += 1
        if arr[k] > arr[j]:
            # 子节点大于父节点，将子节点值赋给父节点
            arr[k], arr[j] = arr[j], arr[k]
        else:
            # 当前不满足，再往上也都已经满足大顶堆，所以直接break
            break
        k = j

# 另一种写法
def shiftDown2(arr, n, k):
    smallest, l, r = k, 2 * k + 1, 2 * k + 2
    while l < n:
        if arr[l] < arr[smallest]:
            smallest = l
        if r < n and arr[r] < arr[smallest]:
            smallest = r
        if smallest == k:
            break
        else:
            arr[k], arr[smallest] = arr[smallest], arr[k]
            k = smallest
            l, r = 2 * k + 1, 2 * k + 2

def heapSort(arr):
    n = len(arr)
    # 构造大顶堆
    for i in reversed(range(n // 2)):
        # 从第一个非叶子节点开始调整
        # 第一个非叶子节点的下标: n / 2 - 1
        shiftDown(arr, n, i)

    # 排序
    for i in range(n - 1, 0, -1):
        # 交换堆顶元素与最后一个元素
        arr[i], arr[0] = arr[0], arr[i]
        shiftDown(arr, i, 0)

# 初始化堆的时候，对于每个非叶子结点，都要调用上述函数，将它与它的孩子结点进行比较和交换，顺序是从后向前。

# 以操作2作为基本操作，对每一层都完全铺满的堆进行分析，

# 设元素个数为n，则堆的高度k=log（n+1）≈log n，非叶子结点的个数为2^（k-1）-1

# 假设每个非叶子结点都需要进行调整，则第i层的非叶子结点需要的操作次数为k-i，

# 第i层共有2^（i-1）个结点，则第i层的所有结点所做的操作为k*2^（i-1）- i*2^（i-1），

# 共k-1层非叶子结点，总的操作次数为 

# sum i=1~k-1 (k*2^（i-1）- i*2^（i-1))

# 化简可得，上式=2^k-k+1，将k=log（n+1）≈log n代入，得n - log n +1，

# 所以，初始化堆的复杂度为O(n)


# 调整堆的复杂度计算和初始化堆差不多，

# 假设根节点和排在最后的序号为m的叶子结点交换，并进行调整，那么调整的操作次数 = 原来m结点所在的层数 = 堆的高度（因为m结点在堆的最后）= log m

# 共n个结点，调整的总操作次数为

# sum m=1~n-1 logm

# 化简可得，上式=log (n-1)! ≈ n*log n

# 所以，调整堆的复杂度为O(n*log n)