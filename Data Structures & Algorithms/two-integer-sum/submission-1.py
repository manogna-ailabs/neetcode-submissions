class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for i, k in enumerate(nums):
            if k in hashmap:
                return [hashmap[k][0], i]
            hashmap[target - k] = (i, k)
