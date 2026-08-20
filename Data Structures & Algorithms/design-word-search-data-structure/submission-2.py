class WordDictionary:
    class Node:
        def __init__(self):
            self.isEnd = False
            self.children = {}

    def __init__(self):
        self.root = self.Node()

    def addWord(self, word: str) -> None:
        nxt = self.root
        for idx, letter in enumerate(word):
            nxt.children.setdefault(letter, self.Node())
            nxt = nxt.children[letter]

        nxt.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(word, cur):
            for idx, letter in enumerate(word):
                if letter == '.':
                    for node in cur.children.values():
                        if dfs(word[idx + 1:], node):
                            return True
                    return False
                else:
                    if letter in cur.children:
                        cur = cur.children[letter]
                    else:
                        return False
            return cur.isEnd
        return dfs(word, self.root)
        