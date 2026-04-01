class Solution:
    def numHours(self, piles, k):
        n = 0
        for b in piles:
            n += (b//k)
            if b % k != 0:
                n += 1
        return n 

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles = sorted(piles)

        l, r = 1, piles[-1]
        mid = (l + r) // 2


        n = self.numHours(piles, mid)
        minS = r

        while l <= r:
            mid = (l + r) // 2
            n = self.numHours(piles, mid)
            if n > h:
                l = mid + 1
            else: 
                minS = mid
                r = mid - 1

        return minS

