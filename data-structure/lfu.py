import collections

# 我们定义两个哈希表，第一个 freq_table 以频率 freq 为索引，
# 每个索引存放一个双向链表，这个链表里存放所有使用频率为 freq 的缓存，
# 缓存里存放三个信息，分别为键 key，值 value，以及使用频率 freq。
# 第二个 key_table 以键值 key 为索引，
# 每个索引存放对应缓存在 freq_table 中链表里的内存地址，
# 这样我们就能利用两个哈希表来使得两个操作的时间复杂度均为 O(1)。
# 同时需要记录一个当前缓存最少使用的频率 minFreq，这是为了删除操作服务的。

# 对于 get(key) 操作，
# 我们能通过索引 key 在 key_table 中找到缓存在 freq_table 中的链表的内存地址，
# 如果不存在直接返回 -1，否则我们能获取到对应缓存的相关信息，
# 这样我们就能知道缓存的键值还有使用频率，直接返回 key 对应的值即可。

# 但是我们注意到 get 操作后这个缓存的使用频率加一了，
# 所以我们需要更新缓存在哈希表 freq_table 中的位置。
# 已知这个缓存的键 key，值 value，以及使用频率 freq，
# 那么该缓存应该存放到 freq_table 中 freq + 1 索引下的链表中。
# 所以我们在当前链表中 O(1) 删除该缓存对应的节点，
# 根据情况更新 minFreq 值，然后将其O(1) 插入到 freq + 1 索引下的链表头完成更新。
# 这其中的操作复杂度均为 O(1)
# 你可能会疑惑更新的时候为什么是插入到链表头，这其实是为了保证缓存在当前链表中从链表头到链表尾的插入时间是有序的，为下面的删除操作服务。

# 对于 put(key, value) 操作，
# 我们先通过索引 key在 key_table 中查看是否有对应的缓存，
# 如果有的话，其实操作等价于 get(key) 操作，唯一的区别就是我们需要将当前的缓存里的值更新为 value。
# 如果没有的话，相当于是新加入的缓存，
# 如果缓存已经到达容量，需要先删除最近最少使用的缓存，再进行插入。

# 先考虑插入，由于是新插入的，所以缓存的使用频率一定是 1，
# 所以我们将缓存的信息插入到 freq_table 中 1 索引下的列表头即可，
# 同时更新 key_table[key] 的信息，以及更新 minFreq = 1。

# 那么剩下的就是删除操作了，
# 由于我们实时维护了 minFreq，所以我们能够知道 freq_table 里目前最少使用频率的索引，
# 同时因为我们保证了链表中从链表头到链表尾的插入时间是有序的，
# 所以 freq_table[minFreq] 的链表中链表尾的节点即为使用频率最小且插入时间最早的节点，
# 我们删除它同时根据情况更新 minFreq ，整个时间复杂度均为 O(1)。


class Node:
    def __init__(self, key, val, pre=None, nex=None, freq=0):
        self.pre = pre
        self.nex = nex
        self.freq = freq
        self.val = val
        self.key = key
        
    def insert(self, nex):
        nex.pre = self
        nex.nex = self.nex
        self.nex.pre = nex
        self.nex = nex
    
def create_linked_list():
    head = Node(0, 0)
    tail = Node(0, 0)
    head.nex = tail
    tail.pre = head
    return (head, tail)

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.minFreq = 0
        self.freqMap = collections.defaultdict(create_linked_list)
        self.keyMap = {}

    def delete(self, node):
        if node.pre:
            node.pre.nex = node.nex
            node.nex.pre = node.pre
            if node.pre is self.freqMap[node.freq][0] and node.nex is self.freqMap[node.freq][-1]:
                self.freqMap.pop(node.freq)
        return node.key
        
    def increase(self, node):
        node.freq += 1
        self.delete(node)
        self.freqMap[node.freq][-1].pre.insert(node)
        if node.freq == 1:
            self.minFreq = 1
        elif self.minFreq == node.freq - 1:
            head, tail = self.freqMap[node.freq - 1]
            if head.nex is tail:
                self.minFreq = node.freq

    def get(self, key: int) -> int:
        if key in self.keyMap:
            self.increase(self.keyMap[key])
            return self.keyMap[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity != 0:
            if key in self.keyMap:
                node = self.keyMap[key]
                node.val = value
            else:
                node = Node(key, value)
                self.keyMap[key] = node
                self.size += 1
            if self.size > self.capacity:
                self.size -= 1
                deleted = self.delete(self.freqMap[self.minFreq][0].nex)
                self.keyMap.pop(deleted)
            self.increase(node)