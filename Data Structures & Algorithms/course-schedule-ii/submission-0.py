class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        preMap = {i: [] for i in range(numCourses)}
        for cls, pre in prerequisites:
            preMap[cls].append(pre)
        
        output = []
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
            output.append(cls)
            return True
        
        for cls in range(numCourses):
            if not valid(cls):
                return []
        
        return output
        