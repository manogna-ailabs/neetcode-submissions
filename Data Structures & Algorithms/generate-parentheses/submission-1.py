class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = []
        def backtrack(path, sum):
            if len(path) == 2*n:
                if sum == 0:
                    out.append(path)
                return
            if sum < 0:
                return
            backtrack(path + "(", sum + 1)
            backtrack(path + ")", sum - 1)
        backtrack("", 0)
        return out