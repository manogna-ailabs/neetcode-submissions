class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        N = len(s)
        result = []
        dp = {}
        def dfs(i, path):
            if i == N:
                result.append(path[1:])
                return True
            out = False
            for j in range(i+1, N+1):
                if s[i:j] in wordSet and dfs(j, path + " "+ s[i:j]): 
                    dp[i] = True
                    out = True
            if out:
                return True
            dp[i] = False
            return False
        dfs(0, "")
        print(dp)
        return result