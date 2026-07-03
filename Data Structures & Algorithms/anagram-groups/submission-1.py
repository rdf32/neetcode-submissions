class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}
        for string in strs:
            rep = [0] * 26
            for c in string:
                rep[ord('a') - ord(c)] += 1
            rep = tuple(rep)
            if rep in groups:
                groups[rep].append(string)
            else:
                groups[rep] = [string]
        
        return list(groups.values())

        # o(n * m) where n is the length of strings and m is the length of longest string