class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        maxChars = 0 
        maxFreq = 0
        charCounts = defaultdict(int)
        while r < len(s):
            charCounts[s[r]] += 1
            maxFreq = max(maxFreq, charCounts[s[r]])
            replaceCount = r - l + 1 - maxFreq

            if replaceCount > k:
                charCounts[s[l]]  -= 1
                l = l + 1

            maxChars = max(maxChars, r - l + 1)
            r = r + 1
        return maxChars
