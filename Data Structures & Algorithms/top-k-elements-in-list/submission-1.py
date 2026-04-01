class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = dict()

        for n in nums:
            count[n] = count.get(n,0) + 1

        arr = [(cnt, num) for num, cnt in count.items()]
        arr.sort(reverse=True)
        return [num for cnt, num in arr[:k]]
