class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for k in range(n+1):
            count = 0
            for i in range(32):
                if (1 << i) & k: # check if ith bit is set
                    count += 1
            res.append(count)
        return res 