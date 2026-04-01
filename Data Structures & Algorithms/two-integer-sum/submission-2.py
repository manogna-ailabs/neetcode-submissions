class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for i, k in enumerate(nums):
            if target - k in hashmap:
                return [hashmap[target-k], i]
            hashmap[k] = i
