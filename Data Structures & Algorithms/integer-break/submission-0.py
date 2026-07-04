class Solution:
    def integerBreak(self, n: int) -> int:
        
        dp = {}
        def dfs(rem):
            if rem in dp:
                return dp[rem]
            if rem == 1:
                return 0
            out = 0
            for i in range(1, rem//2 + 1):
                out_i = max(i, dfs(i)) * max(rem - i, dfs(rem - i))
                out = max(out, out_i)
            dp[rem] = out
            return out
            
        return dfs(n)

# 4
# dfs(1) = 0
# dfs(2) = 2
# dfs(3) = 1 * 2
# dfs(4): possible splits = 1 + 3, 2 + 2, 3 + 1
