class Solution:
    def numDays(self, weights, capacity):
        days = 1
        current = 0
        for w in weights:
            if current + w > capacity:
                days += 1
                current = w
            else:
                current += w
        return days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        best = r
        while l<=r:
            mid = (l+r)//2
            d = self.numDays(weights, mid)
            if d > days:
                l = mid + 1
            else:
                best = mid 
                r = mid - 1
        return best
