class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        def solve(start, end):
            dp = [-1] * n
            def dfs(i):
                if i>end:
                    return 0
                if dp[i] != -1:
                    return dp[i]
                dp[i] = max(nums[i] + dfs(i+2), dfs(i+1))
                return dp[i] 
            return dfs(start)   
        return max(solve(0, n-2), solve(1,n-1))
        