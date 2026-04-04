class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        visited = [False] * n
        def backtrack(path):
            if len(path) == n:
                res.append(path[:])
                return
            for j in range(n):
                if visited[j]:
                    continue
                path.append(nums[j])
                visited[j] = True
                backtrack(path)
                path.pop()
                visited[j] = False


        backtrack([])
        return res