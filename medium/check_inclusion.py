class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        charMap = defaultdict(int)
        s1Map = defaultdict(int)
        for char in s1:
            s1Map[char] += 1
        l = 0 
        r = 0
        while r < len(s2):
            if r - l + 1 <= len(s1):
                charMap[s2[r]] += 1
            else:
                charMap[s2[r]] += 1
                charMap[s2[l]] -= 1
                if charMap[s2[l]] == 0:
                    charMap.pop(s2[l])
                l += 1
            r += 1
            if s1Map == charMap:
                return True
        return False
