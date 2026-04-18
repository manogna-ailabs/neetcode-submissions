class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        def dfs(i):
            if i == n:
                return 1
            if s[i] == "0":
                return 0
            if dp[i] > 0:
                return dp[i]
            dp[i] = dfs(i+1)
            if i+2 <= n and (s[i]=="1" or s[i]=="2" and s[i+1] in "0123456"):
                dp[i] += dfs(i+2)
            return dp[i]

        return dfs(0)
        