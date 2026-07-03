class Node:
    def __init__(self):
        self.endOfWord = False
        self.children = [None] * 26

class PrefixTree:

    def __init__(self):
        self.root = Node()
        
    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            i = ord(c) - ord('a')
            if curr.children[i] == None:
                curr.children[i] = Node()
            curr = curr.children[i]
        curr.endOfWord = True 

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            ind = ord(c) - ord('a')
            if curr.children[ind] == None:
                return False
            curr = curr.children[ind]
        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            ind = ord(c) - ord('a')
            if curr.children[ind] == None:
                return False
            curr = curr.children[ind]
        return True