class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        def evalExp() -> int:
            op = tokens.pop()
            if op != "/" and op != "*" and op != "-" and op != "+":
                return int(op)
            
            right = evalExp()
            left = evalExp()

            if op == "+":
                return right + left
            elif op == "-":
                return left - right
            elif op == "*":
                return left * right
            elif op == "/":
                return int(left / right)
            
        return evalExp()
