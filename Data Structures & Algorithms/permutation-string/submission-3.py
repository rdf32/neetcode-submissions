class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        dist = len(s1)
        s1_counts = self.get_counts(s1)
        for i in range(len(s2) - len(s1) + 1):
            sub = s2[i:dist+i]
            print(sub)
            if s1_counts == self.get_counts(sub):
                return True
        return False
    
    def get_counts(self, s: str) -> dict:
        counts = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1
        return counts