class Node:
    def __init__(self):
        self.word = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = Node()
    
    def add(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.word = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        tri = Trie()
        for word in words:
            tri.add(word)
        
        rows, cols = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if (r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visit or 
                board[r][c] not in node.children):
                return False
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.word:
                res.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, tri.root, "")
        
        return list(res)
        
   


        