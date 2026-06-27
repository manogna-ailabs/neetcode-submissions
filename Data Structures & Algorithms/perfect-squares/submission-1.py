class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1
        
        dp = {}
        # def dfs(rem):
        #     if rem == 0:
        #         return 0
        #     if rem in dp:
        #         return dp[rem]
        #     dp[rem] = rem
        #     for square in squares:
        #         if square > rem:
        #             break
        #         dp[rem] = min(1 + dfs(rem-square), dp[rem])
        #     return dp[rem]

        dp[0] = 0
        for rem in range(1, n+1):
            dp[rem] = rem
            for square in squares:
                if square > rem:
                    break
                dp[rem] = min(1 + dp[rem-square], dp[rem])

        return dp[n] 