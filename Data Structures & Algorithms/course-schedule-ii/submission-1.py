class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        pre_map = {i: [] for i in range(numCourses)}
        for cls, pre in prerequisites:
            pre_map[cls].append(pre)
        

        taken = set()
        cycle = set()
        output = []

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in taken:
                return True
            
            cycle.add(crs)
            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)

            taken.add(crs)
            output.append(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return output

   
