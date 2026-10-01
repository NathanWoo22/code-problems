
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCharCount = defaultdict(int)
        windowChars = defaultdict(int)
        for char in t:
            tCharCount[char] += 1
        
        l = 0
        r = 0
        minSub = ""
    
        while r < len(s):
            if r == 0:
                windowChars[s[r]] += 1
            valid = True
            for char, num in tCharCount.items(): 
                if windowChars[char] < num:
                    valid = False
                    break
            if valid:
                if r - l + 1 < len(minSub) or len(minSub) == 0:
                    minSub = s[l:r + 1]
            
            if valid and l < r:
                windowChars[s[l]] -= 1
                l += 1
            else: 
                r += 1
                if r < len(s):
                    windowChars[s[r]] += 1
        return minSub
