class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        memo = {}

        cumSum = [0] * (n+1)
        for i in range(1, n+1):
            cumSum[i] = cumSum[i-1] + nums[i-1]

        def dfs(i, k):
            if k == 1:
                return cumSum[-1] - cumSum[i]     # sum(nums[i:])
            if (i,k) in memo:
                return memo[(i,k)]
            best_sum = float('inf')
            for end in range(i+1, n-k+2):
                curr_sum = cumSum[end] - cumSum[i] #sum(nums[i:end])
                rem_sum = dfs(end, k-1)
                max_sum = max(curr_sum, rem_sum)
                best_sum = min(best_sum, max_sum)
            memo[(i, k)] = best_sum
            return best_sum

        return dfs(0, k)