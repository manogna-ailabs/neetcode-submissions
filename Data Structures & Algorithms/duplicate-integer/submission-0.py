class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = dict()
        for k in nums:
            hashmap[k] = hashmap.get(k,0) + 1
            if hashmap[k]>1:
                return True
        
        return False