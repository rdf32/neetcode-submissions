class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) > (n - 1):
            return False

        edgeMap = {i: [] for i in range(n)}
        for a, b in edges:
            edgeMap[a].append(b)
            edgeMap[b].append(a) ## undirected so need to track both

        print(edgeMap)
        # adj = [[] for _ in range(n)]
        # for u, v in edges:
        #     adj[u].append(v)
        #     adj[v].append(u)
        # print(adj)
        cycle = set()
        def dfs(node, parent):
            if node in cycle:
                return False ## checking for cycles

            cycle.add(node)
            for nei in edgeMap[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False

            return True
        
        
        return dfs(0, -1) and len(cycle) == n



            
