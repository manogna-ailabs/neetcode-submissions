class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for i in range(32):
            if (1 << i) & n:
                res += 1
        return res

        res = 0
        while n:
            res += 1 if n & 1 else 0 # check if LSB is 1
            n >>= 1 # right shift bits in n
        return res

        res = 0
        while n:
            n = n & (n - 1)
            res += 1
        return res