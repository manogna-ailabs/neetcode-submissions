class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        check = 1
        nums.sort()
        nums = set(nums)
        for n in nums:
            if n > 0 and n == check:
                check += 1
        return check