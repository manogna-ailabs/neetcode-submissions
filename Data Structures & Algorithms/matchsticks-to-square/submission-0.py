class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        target = sum(matchsticks) // 4
        if sum(matchsticks) % 4 != 0:
            return False
        matchsticks.sort(reverse=True)
        if matchsticks[0] > target:
            return False
        
        N = len(matchsticks)
        sides = [0] * 4

        def getSides(i):
            if i == N:
                return True
            for k in range(4):
                if sides[k] + matchsticks[i] > target:
                    continue
                
                sides[k] += matchsticks[i]
                if getSides(i+1):
                    return True
                sides[k] -= matchsticks[i]

                if sides[k] == 0:
                    break
            return False
        
        return getSides(0)
        