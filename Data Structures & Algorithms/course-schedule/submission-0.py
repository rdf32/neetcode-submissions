class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        preMap = {i: [] for i in range(numCourses)}
        for cls, pre in prerequisites:
            preMap[cls].append(pre)
        
        visited = set()

        def dfs(cls):
            if cls in visited:
                return False
            
            if preMap[cls] == []:
                return True

            visited.add(cls)
            for pre in preMap[cls]:
                if not dfs(pre):
                    return False
            visited.remove(cls)
            preMap[cls] = []
            
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
        