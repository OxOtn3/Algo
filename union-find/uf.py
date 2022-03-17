class UF:
    def __init__(self, sz):
        self.parent = list(range(sz))
        self.compo = sz

    def find(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xRoot, yRoot = self.find(x), self.find(y)
        if xRoot == yRoot: return
        self.parent[xRoot] = yRoot
        self.compo -= 1
    
    def isConnected(self, x, y):
        return self.find(x) == self.find(y)