class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded = encoded + str(len(string)) + "#" + string
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i >= 0 and i < len(s) - 1:
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            decoded.append(s[j+1:j+length+1])
            i = j + length + 1
        return decoded