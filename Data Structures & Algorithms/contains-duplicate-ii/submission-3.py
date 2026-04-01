class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        l, r = 0, 1
        while r < len(nums):
            while r - l <= k and r < len(nums):
                if nums[l] == nums[r]:
                    return True
                r += 1
            l += 1
            r = l+1
        return False 