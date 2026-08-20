class PrefixTree:
    class Node:
        def __init__(self, val = ""):
            self.val = val
            self.children = {}

    def __init__(self):
        self.root = self.Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for i, c in enumerate(word):
            nxt = cur.children.setdefault(c, self.Node(""))
            cur = nxt
        cur.val = word

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            nxt = cur.children.get(c, None)
            if nxt is None:
                return False
            cur = nxt
        return cur.val == word

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            nxt = cur.children.get(c, None)
            if nxt is None:
                return False
            cur = nxt
        return True
        