class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        res = []
        digitToChar = {
                    "2": "abc",
                    "3": "def",
                    "4": "ghi",
                    "5": "jkl",
                    "6": "mno",
                    "7": "qprs",
                    "8": "tuv",
                    "9": "wxyz",
                }

        built = []
        def recurse(i):
            nonlocal built
            if i >= len(digits):
                res.append(built.copy())
                return 

            for digit in digitToChar[digits[i]]:
                built.append(digit)
                recurse(i + 1)
                built.pop()
        
        recurse(0)
        return ["".join(x) for x in res]
            
            
