class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        check = 1
        nums.sort()
        nums = set(nums)
        # print(nums)
        for n in nums:
            if n > 0:
                if n == check:
                    check += 1
                # else:
                    # return check
        return check