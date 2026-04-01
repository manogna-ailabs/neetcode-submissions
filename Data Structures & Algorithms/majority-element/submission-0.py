class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = dict()
        out, maxCount = 0, 0

        for i, n in enumerate(nums):
            count[n] = count.get(n,0) + 1
            if count[n] > maxCount:
                out = n
                maxCount = count[n]
        return out