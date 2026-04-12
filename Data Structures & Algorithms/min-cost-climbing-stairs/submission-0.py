class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        best = float("inf")
        cache = [-1] * n
        def dfs(i):
            if i == n:
                return 0
            if i > n:
                return float("inf")
            if cache[i] != -1:
                return cache[i]
            cache[i] = min(cost[i] + dfs(i+1), cost[i] + dfs(i+2))
            return cache[i]

        return min(dfs(0), dfs(1))