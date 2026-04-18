class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        res = set()
        thresh = len(nums)//3
        for n in nums:
            count[n] = count.get(n,0) + 1
            if count[n] > thresh:
                res.add(n)
        return list(res)
