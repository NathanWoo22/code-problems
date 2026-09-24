class Solution:
    def isValid(self, s: str) -> bool:
        sta = []
        for i, val in enumerate(s):
            if val == "(" or val == "{" or val == "[":
                sta.append(val)
            elif len(sta) == 0:
                return False
            elif val == ")" and sta[-1] == "(":
                sta.pop()
            elif val == "}" and sta[-1] == "{":
                sta.pop()
            elif val == "]" and sta[-1] == "[":
                sta.pop()
            else:
                return False
            
        if len(sta) != 0:
            return False
        return True
