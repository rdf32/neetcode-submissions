class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = []
        store = {}
        for s in strs:
            encoded = self.encode(s)
            if tuple(encoded) in store:
                store[tuple(encoded)].append(s)
            else:
                store[tuple(encoded)] = [s]
        
        return list(store.values())

        


    def encode(self, s):

        array = [0] * 26
        for c in s:
            array[ord('a') - ord(c)] += 1
        
        return array