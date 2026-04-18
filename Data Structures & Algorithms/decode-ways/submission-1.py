class Solution:
    def numDecodings(self, s: str) -> int:
        res = 0
        n = len(s)
        dp = [0] * n
        def dfs(i, path):
            nonlocal res 
            if i == n:
                res += 1
                return 1
            if i>n :
                return 0
            if s[i] == "0":
                return 0
            if dp[i] > 0:
                return dp[i]
            dp[i] = dfs(i+1, path +[s[i]])
            if int(s[i:i+2]) < 27:
                dp[i] += dfs(i+2, path + [s[i:i+2]])
            return dp[i]

        return dfs(0, [])
        return res
        