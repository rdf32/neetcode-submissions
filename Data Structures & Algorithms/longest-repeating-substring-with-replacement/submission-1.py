class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        result = 0
        counts = {}

        max_freq = 0
        left     = 0
        for right in range(len(s)):
            counts[s[right]] = counts.get(s[right], 0) + 1     ## increment count for letter
            max_freq         = max(max_freq, counts[s[right]]) ## get curr max frequency

            while (right - left + 1) - max_freq > k:
                counts[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
        
        return result


        