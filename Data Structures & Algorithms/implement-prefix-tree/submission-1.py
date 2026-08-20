class PrefixTree:
    class Node:
        def __init__(self, isEnd = False):
            self.isEnd = isEnd
            self.children = {}

    def __init__(self):
        self.root = self.Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for i, c in enumerate(word):
            nxt = cur.children.setdefault(c, self.Node(False))
            cur = nxt
        cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            nxt = cur.children.get(c, None)
            if nxt is None:
                return False
            cur = nxt
        return cur.isEnd == True

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            nxt = cur.children.get(c, None)
            if nxt is None:
                return False
            cur = nxt
        return True
        