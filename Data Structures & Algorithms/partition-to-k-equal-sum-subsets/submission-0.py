class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False

        target_ssum = total_sum // k
        nums.sort(reverse = True)
        n = len(nums)
        visit = [False] * n

        def dfs(i, k_remaining, curr_sum):
            if k_remaining == 0:
                return True
            if curr_sum == target_ssum:
                return dfs(0, k_remaining - 1, 0)

            for j in range(i, n):
                if visit[j]:
                    continue
                if curr_sum + nums[j] > target_ssum:
                    continue
                visit[j] = True
                if dfs(j + 1, k_remaining, curr_sum + nums[j]):
                    return True
                visit[j] = False
            return False

        return dfs(0, k, 0)


