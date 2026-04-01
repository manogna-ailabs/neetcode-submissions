class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for op in operations:
            if op == "+":
                a = scores[-1] + scores[-2]
                scores.append(a)
            elif op == "C":
                scores.pop(-1)
            elif op == "D":
                scores.append(scores[-1]*2)
            else:
                scores.append(int(op))
        return sum(scores)