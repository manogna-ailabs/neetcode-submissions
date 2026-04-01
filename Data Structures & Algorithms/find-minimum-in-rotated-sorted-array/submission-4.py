class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        i = 0
        while l <= r:
            mid = (l+r)//2
            print(nums[l], nums[mid], nums[r])
            if nums[l] <= nums[r]:
                return nums[l]
            elif nums[mid] > nums[r]:
                l = mid+1
            elif nums[mid] < nums[l]:
                l += 1
            # i+=1
        return nums[l]

