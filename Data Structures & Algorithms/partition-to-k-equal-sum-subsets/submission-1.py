class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False

        target_ssum = total_sum // k
        nums.sort(reverse = True)
        n = len(nums)

        if nums[0] > target_ssum:
            return False

        # Optimal
        bucket = [0] * k        # subset-sum

        def backtrack(i):
            if i == n:
                return True

            for j in range(k):
                if bucket[j] + nums[i] > target_ssum:
                    continue
                
                bucket[j] += nums[i]    # add

                if backtrack(i+1):      # explore
                    return True
                
                bucket[j] -= nums[i]    # undo

                if bucket[j] == 0:      # prune subsets starting from 0
                    break

            return False
        return backtrack(0)


        # Mine
        # visit = [False] * n

        # def dfs(i, k_remaining, curr_sum):
        #     if k_remaining == 0:
        #         return True
        #     if curr_sum == target_ssum:
        #         return dfs(0, k_remaining - 1, 0)

        #     for j in range(i, n):
        #         if visit[j]:
        #             continue
        #         if curr_sum + nums[j] > target_ssum:
        #             continue
        #         visit[j] = True
        #         if dfs(j + 1, k_remaining, curr_sum + nums[j]):
        #             return True
        #         visit[j] = False
        #     return False

        # return dfs(0, k, 0)


