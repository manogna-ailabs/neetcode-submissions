class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-k for k in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            a = heapq.heappop(stones)
            b = heapq.heappop(stones)
            if a != b:
                diff = a - b
                heapq.heappush(stones, diff)
        
        return 0 if not stones else -stones[0]
