class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums = set(nums)
        dp = {}


        def dfs(target):
            if target < 0:
                return 0
            if target == 0:
                return 1 
            if target in dp:
                return dp[target]
            n_ways = 0
            for n in nums:
                n_ways += dfs(target - n)
            dp[target] = n_ways
            return n_ways
        return dfs(target)
