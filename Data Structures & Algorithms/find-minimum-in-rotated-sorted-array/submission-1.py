class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r  = 0, len(nums) - 1 
        if nums[l] < nums[r]:
            return nums[l]

        while l<r:
            mid = (l+r) // 2
            if nums[r] < nums[mid]:
                l += 1
            elif nums[l] > nums[mid]:
                r -= 1

        return min(nums[l], nums[r])
