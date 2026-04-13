class Solution:
    def rob(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        dp = [0] * n
        def dfs(i):
            if i>=n:
                return 0
            if dp[i] > 0:
                return dp[i]
            dp[i] = max(nums[i] + dfs(i+2), dfs(i+1)) 
            return dp[i]

        return max(dfs(0), dfs(1))