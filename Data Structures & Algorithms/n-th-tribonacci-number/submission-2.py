class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0 or n==1:
            return n
        dp = [0] * (n+1)
        dp[1], dp[2] = 1, 1
        if n >= 3:
            for i in range(3,n+1):
                dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        return dp[n]

        t = [0, 1, 1]
        if n < 3:
            return t[n]
        for i in range(3, n+1):
            t[i % 3] = sum(t)
        return t[n % 3]
