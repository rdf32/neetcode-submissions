class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        edgeMap = {i: [] for i in range(n)}
        for a, b in edges:
            edgeMap[a].append(b)
            edgeMap[b].append(a)
        

        visit = set()
        def dfs(node):
            for nei in edgeMap[node]:
                if nei not in visit:
                    visit.add(nei)
                    dfs(nei)
        
        total = 0
        for node in range(n):
            if node not in visit:
                visit.add(node)
                dfs(node)
                total += 1
        
        return total

            

        