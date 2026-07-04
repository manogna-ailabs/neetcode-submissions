class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1
        ans = x
        bit = 0

        while n:
            if (x >> bit) & 1 == 0:
                if n & 1:
                    ans |= 1 << bit
                n >>= 1
            bit += 1

        return ans
        
        res = 0
        n -= 1
        x_bin = [0] * 64
        n_bin = [0] * 64
        for i in range(32):
            x_bin[i] = (x>>i) & 1
            n_bin[i] = (n>>i) & 1
        
        i_x = 0
        i_n = 0
        while i_x < 63:
            while i_x < 63 and x_bin[i_x] != 0:
                i_x += 1
            x_bin[i_x] = n_bin[i_n]
            i_x += 1
            i_n += 1
        for i in range(64):
            if x_bin[i] == 1:
                res += (1<<i)
        return res


        res = x
        for i in range(n-1):
            res = (res + 1) | x
        return res