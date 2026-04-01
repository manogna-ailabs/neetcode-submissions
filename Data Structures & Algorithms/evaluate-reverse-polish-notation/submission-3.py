class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ["+", "-", "*", "/"]
        ops = {"+" : lambda a, b: a + b,
               "-" : lambda a, b: a - b,
               "*" : lambda a, b: a * b,
               "/" : lambda a, b: int(a/b) }
        stack = []
        for i, token in enumerate(tokens):
            stack.append(token)
            while stack and stack[-1] in ops:
                print(stack)
                op = stack.pop()
                b = int(stack.pop())
                a = int(stack.pop())
                ans = ops[op](a, b)
                stack.append(ans)
                print(a, b, op, ans)
        ans = int(stack.pop())
        return ans
