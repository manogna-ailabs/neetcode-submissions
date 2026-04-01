class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if nums == []:
            return 0

        nums = sorted(nums)

        maxlength = 1

        diff = []
        for i in range(1,len(nums)):
            diff.append(nums[i] - nums[i-1])

        i = 0
        l = 1

        while i < len(diff):
            if diff[i] > 1:
                l = 1 
            elif diff[i] == 1:
                l += 1
            if l > maxlength:
                maxlength = l
            i += 1

        return maxlength 