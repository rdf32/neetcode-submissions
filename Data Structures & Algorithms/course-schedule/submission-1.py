class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


        preMap = {i: [] for i in range(numCourses)}
        for cls, pre in prerequisites:
            preMap[cls].append(pre)
        
        cycle, taken = set(), set()
        def valid(cls):

            if cls in cycle:
                return False
            
            if cls in taken:
                return True
            
            cycle.add(cls)
            for pre in preMap[cls]:
                if not valid(pre):
                    return False
            
            cycle.remove(cls)
            taken.add(cls)

            return True
        
        for cls in range(numCourses):
            if not valid(cls):
                return False
        return True
        