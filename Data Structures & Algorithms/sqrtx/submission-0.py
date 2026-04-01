class Solution:
    def mySqrt(self, x: int) -> int:
        l = 1
        r = x
        res = 0
        while l<=r:
            mid = (l+r)//2
            if mid ** 2 > x:
                r = mid - 1
            elif mid ** 2 < x:
                l = mid + 1
                res = mid
            else:
                return mid
        return res
        