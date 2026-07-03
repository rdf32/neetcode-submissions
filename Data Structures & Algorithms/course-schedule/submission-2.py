class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        pre_map = {crs: [] for crs in range(numCourses)}
        for cls, pre in prerequisites:
            pre_map[cls].append(pre)

        cycle = set()
        taken = set()

        def dfs(crs):
            if crs in taken:
                return True
            
            if crs in cycle:
                return False
            
            cycle.add(crs)
            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            taken.add(crs)
        
            return True
        
        for cls in range(numCourses):
            if not dfs(cls):
                return False
        return True
            