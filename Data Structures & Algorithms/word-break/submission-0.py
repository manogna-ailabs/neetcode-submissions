class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        N = len(s)
        dp = {}

        def dfs(i):
            if i == N:
                return True
            if i in dp:
                return dp[i]

            for end in range(i + 1, N + 1):
                if s[i:end] in wordSet and dfs(end):
                    dp[i] = True
                    return True
            dp[i] = False
            return False

        return dfs(0)

