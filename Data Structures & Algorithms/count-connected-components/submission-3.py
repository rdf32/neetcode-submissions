class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj_map = {i: [] for i in range(n)}
        for u, v in edges:
            adj_map[u].append(v)
            adj_map[v].append(u)
        

        visited = set()
        def dfs(node):
            for nei in adj_map[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)
        
        total = 0
        for node in range(n):
            if node not in visited:
                visited.add(node)
                dfs(node)
                total += 1
        return total
        
