class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCharCount = defaultdict(int)
        windowChars = defaultdict(int)
        for char in t:
            tCharCount[char] += 1
        tCount  = len(tCharCount)
        formed = 0        
        l = 0
        r = 0
        minSub = ""
    
        while r < len(s):
            if r == 0:
                windowChars[s[r]] += 1
                if tCharCount[s[r]] == windowChars[s[r]]:
                    formed += 1 
            
            valid = formed == tCount
            if valid:
                if r - l + 1 < len(minSub) or len(minSub) == 0:
                    minSub = s[l:r + 1]
            
            if valid and l < r:
                windowChars[s[l]] -= 1
                if tCharCount[s[l]] == windowChars[s[l]] + 1:
                    formed -= 1
                l += 1
            else: 
                r += 1
                if r < len(s):
                    windowChars[s[r]] += 1
                    if tCharCount[s[r]] == windowChars[s[r]]:
                        formed += 1 
        return minSub
