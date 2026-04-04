class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        out = []
        def dfs(i, val):

            if i == len(nums):
                return out
            if val and sum(val) == target:
                out.append(val)
                return
            if val and sum(val) > target:
                return
            
            dfs(i, val + [nums[i]])  
            dfs(i+1, val)                
        dfs(0, [])
        return out

