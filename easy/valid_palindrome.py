class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanStr = ""
        revStr = ""
        for char in s:
            if char.isalnum():
                cleanStr = cleanStr + char
                revStr = char + revStr
        
        cleanStr = cleanStr.lower()
        revStr = revStr.lower()

        return cleanStr == revStr
