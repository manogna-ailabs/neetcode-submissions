class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = {}
        N = len(stoneValue)
        print(N)
        suffixSum = [0] * N
        suffixSum[N-1] = stoneValue[N-1]
        for k in range(N-2,-1,-1):
            suffixSum[k] = stoneValue[k] + suffixSum[k+1]
        def dfs(i):
            if i == N:
                return 0
            if i in dp:
                return dp[i]
            remSum = suffixSum[i]
            if i+1 <= N:
                out = remSum - dfs(i+1)
            if i + 2 <= N:
                out = max(out, remSum - dfs(i+2))
            if i + 3 <= N:
                out = max(out, remSum - dfs(i+3))
            dp[i] = out
            return dp[i]
        if N > 1000:
            dfs(900)
        aliceScore =  dfs(0)
        bobScore = sum(stoneValue) - aliceScore
        if aliceScore > bobScore:
            return "Alice"
        elif bobScore > aliceScore:
            return "Bob"
        else:
            return "Tie"
