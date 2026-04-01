class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap1, hashmap2 = dict(), dict()
        for ch1, ch2 in zip(s, t):
            hashmap1[ch1] = hashmap1.get(ch1, 0) + 1
            hashmap2[ch2] = hashmap2.get(ch2, 0) + 1
        
        for ch1 in hashmap1:
            if ch1 not in hashmap2:
                return False
            if hashmap1[ch1] != hashmap2[ch1]:
                return False

        return True
