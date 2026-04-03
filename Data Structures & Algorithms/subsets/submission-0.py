class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []
        def dfs(idx, val):
            if idx == len(nums):
                out.append(val)
                return
            dfs(idx+1, val) 
            dfs(idx+1, val+[nums[idx]])
        dfs(0, [])
        return out