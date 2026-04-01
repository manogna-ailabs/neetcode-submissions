class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r  = 0, len(nums) - 1 

        while l<=r:
            m = (l+r)//2
            print(nums[l], nums[m], nums[r])
            if target == nums[m]:
                return m
            elif target < nums[m]:
                if target >= nums[l]:
                    r = m - 1
                else:
                    l = l + 1
            elif target > nums[m]:
                if target <= nums[r]:
                    l = m + 1
                else:
                    r = r - 1

        return m if target == nums[m] else -1