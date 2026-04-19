class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}

        def dfs(rem):
            if rem==0:
                return 0
            if rem < 0:
                return float('inf')
            if rem in dp:
                return dp[rem]
            res = float('inf')
            for c in coins:
                res = min(res, 1+dfs(rem-c))
            dp[rem] = res
            return res
        ans = dfs(amount)
        return ans if ans!=float('inf') else -1