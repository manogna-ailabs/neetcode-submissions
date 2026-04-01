class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {"+" : lambda a, b: a + b,
               "-" : lambda a, b: a - b,
               "*" : lambda a, b: a * b,
               "/" : lambda a, b: int(a/b) }
        stack = []
        for i, token in enumerate(tokens):
            if token in ops:
                b = stack.pop()
                a = stack.pop()
                ans = ops[token](a, b)
                stack.append(ans)
            else:
                stack.append(int(token))
        return stack.pop()
