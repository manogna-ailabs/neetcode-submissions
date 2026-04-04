class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        visited = [False] * n
        def backtrack(path):
            if len(path) == n:
                res.append(path[:])
                return
            for i in range(n):
                if visited[i]:
                    continue
                if i>0 and nums[i] == nums[i-1] and not visited[i-1]:
                    continue
                path.append(nums[i])
                visited[i] = True
                backtrack(path)
                path.pop()
                visited[i] = False
        backtrack([])
        return res

