class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Max heap (-stones + min heap)
        # stones = [-k for k in stones]
        # heapq.heapify(stones)

        # while len(stones) > 1:
        #     a = heapq.heappop(stones)
        #     b = heapq.heappop(stones)
        #     if a != b:
        #         diff = a - b
        #         heapq.heappush(stones, diff)
        
        # return 0 if not stones else -stones[0]

        # Bucket sort
        maxWeight = max(stones)
        bucket = [0] * (maxWeight + 1)
        for w in stones:
            bucket[w] += 1

        first = second = maxWeight
        while first > 0:
            if bucket[first] % 2 == 0:
                first -= 1
                continue
            
            j = min(first - 1, second)
            while j > 0 and bucket[j] == 0:
                j -= 1
            
            if j == 0:
                return first

            second = j
            bucket[first] -= 1
            bucket[second] -= 1
            bucket[first - second] += 1

            first = max(second, first - second)
        return 0

        
