# 显然，我们更关心元素的频率。令 freq 作为 xx 到 xx 的出现次数的映射 Map。

# 此外，我们也（可能）关心 maxfreq，即栈中任意元素的当前最大频率。这是理所应当的事情，因为我们必须弹出频率最高的元素。

# 那么当前主要的问题就变成了：在具有相同的（最大）频率的元素中，怎么判断那个元素是最新的？我们可以使用栈来查询这一信息：靠近栈顶的元素总是相对更新一些。

# 为此，我们令 group 作为从频率到具有该频率的元素的映射。到目前，我们已经实现了 FreqStack 的所有必要的组件。

# 实际上，作为实现层面上的一点细节，如果 x 的频率为 f，那么我们将获取在所有 group[i] (i <= f) 中的 x,而不仅仅是栈顶的那个。这是因为每个 group[i] 都会存储与第 i 个 x 副本相关的信息。

# 此后，我们仅仅需要如上所述维护 freq，group，以及 maxfreq。

import collections


class FreqStack(object):

    def __init__(self):
        self.freq = collections.Counter()
        self.group = collections.defaultdict(list)
        self.maxfreq = 0

    def push(self, x):
        f = self.freq[x] + 1
        self.freq[x] = f
        if f > self.maxfreq:
            self.maxfreq = f
        self.group[f].append(x)

    def pop(self):
        x = self.group[self.maxfreq].pop()
        self.freq[x] -= 1
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1

        return x