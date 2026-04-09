class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        d2a = {"2": "abc", "3":"def", "4": "ghi", "5": "jkl", "6":"mno",
                "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        n = len(digits)

        def backtrack(i, path):
            if i == n:
                res.append(path)
                return
            for ch in d2a[digits[i]]:
                backtrack(i+1, path+ch)

        backtrack(0,"")
        return res

    