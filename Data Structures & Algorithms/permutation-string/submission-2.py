class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_set = sorted(s1)
        print(s1_set)

        k = len(s1)
        for i in range(len(s2)-k+1):
            subset = sorted(s2[i:i+k])
            if s1_set == subset:
                return True
        return False