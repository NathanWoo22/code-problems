class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        charSet = set()
        l = 0
        r = 0
        while r < len(s):
            if s[r] not in charSet:
                maxLen = max(maxLen, r - l + 1)
                charSet.add(s[r])
                r += 1
            else: 
                while s[l] != s[r]:
                    charSet.remove(s[l])
                    l += 1
                charSet.remove(s[l])
                l += 1
        return maxLen
