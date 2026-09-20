
class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        for string in strs:
            encodedStr += str(len(string)) + "#" + string

        return encodedStr
    

    def decode(self, s: str) -> List[str]:
        tip = 0
        lenReader = 0
        decodedStrs = []
        while tip < len(s):
            lenNext = ""
            print(tip)
            while s[tip + lenReader] != "#":
                lenNext += s[tip + lenReader]
                lenReader += 1
            lenReader += 1
            print(lenNext)
            decodedStrs.append(s[tip + lenReader : tip + lenReader + int(lenNext)])

            tip = lenReader + tip + int(lenNext)
            lenReader = 0

        return decodedStrs
