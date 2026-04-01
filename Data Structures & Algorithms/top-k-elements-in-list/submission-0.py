class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = dict()

        for n in nums:
            count[n] = count.get(n,0) + 1

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        out = []
        for i in range(k):
            out.append(arr.pop()[1])

        return(out)

        out = list(count_sorted.keys())[:k]

        return out
