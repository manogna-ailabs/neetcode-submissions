class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustmap = {}
        for (a,b) in trust:
            if b not in trustmap:
                trustmap[b] = [a]
            trustmap[b] = trustmap[b] + [b]
        if len(trustmap) > 1:
            return -1
        return b 