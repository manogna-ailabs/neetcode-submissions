class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = {}
        n = len(nums)
        res = float("-inf")
        for l in range(n):
            for r in range(l, n):
                if l == r:
                    dp[(l,r)] = nums[l]
                elif (l,r - 1) in dp:
                    dp[(l,r)] = dp[(l, r - 1)] * nums[r]
                res = max(res, dp[(l,r)])
        return res