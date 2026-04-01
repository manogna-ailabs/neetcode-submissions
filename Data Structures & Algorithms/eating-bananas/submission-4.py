class Solution:
    def numHours(self, piles, k):
        n = 0
        for b in piles:
            n += (b//k)
            if b % k != 0:
                n += 1
        return n 

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        best = max(piles)
        while l<=r:
            mid = (l+r)//2
            n_mid = self.numHours(piles, mid)
            print(mid, n_mid)
            if n_mid > h:
                l = mid + 1
            elif n_mid <=h:
                r = mid -1
                best = min(mid, best) 
            # return
        return best

