class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {0:1}
        cumsum  = 0
        count = 0

        for num in nums:
            cumsum += num

            if cumsum-k in prefixSum:
                count += prefixSum[cumsum-k]
            
            prefixSum[cumsum] = prefixSum.get(cumsum, 0) + 1
        
        return count

