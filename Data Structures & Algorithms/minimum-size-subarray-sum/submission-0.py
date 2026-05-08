class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        minL = float("inf")
        for l in range(n):
            arraySum = 0
            for r in range(l, n):
                arraySum += nums[r]
                if arraySum >= target:
                    minL = min(minL, r - l + 1)
                    break
        return 0 if minL == float("inf") else minL 