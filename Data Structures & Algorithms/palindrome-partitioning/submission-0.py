class Solution:
    def partition(self, s: str) -> List[List[str]]:
        out = []
        n = len(s)
        def backtrack(start, res):
            nonlocal n
            if start == n:
                out.append(res[:])
            for end in range(start+1, n+1):
                t = s[start:end]
                if t == t[::-1]:
                    backtrack(end, res + [t])
        backtrack(0, [])
        return out