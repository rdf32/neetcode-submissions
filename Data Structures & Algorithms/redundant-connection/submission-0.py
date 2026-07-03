class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        edgeMap = {i: [] for i in range(len(edges) + 1)}

        def dfs(node, par):
            if node in visit:
                return True

            visit.add(node)
            for nei in edgeMap[node]:
                if nei == par:
                    continue
                if dfs(nei, node):
                    return True
            return False
        

        for u, v in edges:
            edgeMap[u].append(v)
            edgeMap[v].append(u)
            visit = set()
        
            if dfs(u, -1):
                return [u, v]

        