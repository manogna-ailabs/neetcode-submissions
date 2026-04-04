class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def backtrack(i, path):
            if len(path) == n:
                res.append(path[:])
                return
            for j in range(n):
                if nums[j] not in path:
                    path.append(nums[j])
                    backtrack(j+1 ,path)
                    path.pop()

        backtrack(0, [])
        return res