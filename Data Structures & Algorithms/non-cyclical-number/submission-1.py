class Solution:
    def isHappy(self, n: int) -> bool:
        def squaresum(k):
            s = 0
            while k:
                digit = k % 10
                s += digit ** 2
                k = k//10
            return s

        s_dict = set()
        k = n
        t = 1
        while k not in s_dict:
            s_dict.add(k)
            k = squaresum(k)
            if k == 1:
                return True
        return False

