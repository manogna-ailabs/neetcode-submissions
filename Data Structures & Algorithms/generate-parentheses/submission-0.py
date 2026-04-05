class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = []
        val = {"(" : 1, ")" : -1}
        def backtrack(path, sum):
            if len(path) == 2*n and sum == 0:
                out.append(path)
                return
            if sum < 0 or len(path) == 2*n:
                return
            
            backtrack(path + "(", sum + 1)
            backtrack(path + ")", sum - 1)

        backtrack("", 0)
        return out