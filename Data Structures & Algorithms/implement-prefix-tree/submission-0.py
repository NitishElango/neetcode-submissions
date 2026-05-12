class TrieNode():
    def __init__(self):
        self.children = dict()
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
                cur = cur.children[c]
            else:
                cur = cur.children[c]
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for i in range(len(word)):
            c = word[i]
            if c in cur.children:
                if i == len(word) - 1:
                    if cur.children[c].end:
                        return True
                    else:
                        return False
                else:
                    cur = cur.children[c]
            else:
                return False
        return True

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False
        return True
        
        