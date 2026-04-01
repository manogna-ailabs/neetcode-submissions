class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        out = []

        for i, a in enumerate(nums):
            if a > 0:
                break
            l = i + 1
            r = len(nums) - 1
            if i > 0 and a == nums[i-1]:
                continue

            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r = r - 1
                elif threeSum < 0:
                    l = l + 1
                else:
                    out.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return out

