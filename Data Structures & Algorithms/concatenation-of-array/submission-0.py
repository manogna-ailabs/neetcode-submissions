class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*2*n
        for i, k in enumerate(nums):
            ans[i] = k
            ans[i+n] = k
        return ans