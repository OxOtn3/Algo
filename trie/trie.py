# 小写字母的前缀树

class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            i = ord(ch) - ord("a")
            if not node.children[i]:
                node.children[i] = Trie()
            node = node.children[i]
        node.isEnd = True
    
    def searchPrefix(self, prefix: str) -> "Trie":
        node = self
        for ch in prefix:
            i = ord(ch) - ord("a")
            if not node.children[i]:
                return None
            node = node.children[i]
        return node

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node is not None and node.isEnd

    def startsWith(self, prefix: str) -> bool:
        return self.searchPrefix(prefix) is not None