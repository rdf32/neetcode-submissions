class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adj_map = {i: [] for i in range(n)}
        for u, v in edges:
            adj_map[u].append(v)
            adj_map[v].append(u)
        
        cycle = set()
        def dfs(node, par):
            if node in cycle:
                return False
            
            cycle.add(node)
            for nei in adj_map[node]:
                if nei == par:
                    continue
                if not dfs(nei, node):
                    return False
            return True

        return dfs(0, -1) and len(cycle) == n
        