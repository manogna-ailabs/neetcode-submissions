class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 0
        n = len(nums)
        while j<n:
            nums[i] = nums[j]
            while j<n and nums[i]==nums[j]:
                j +=1
            i+=1
        return i