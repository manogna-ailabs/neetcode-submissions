class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = dict()

        for word in strs:
            sorted_word = "".join(sorted(word))
            count[sorted_word] = count.get(sorted_word, []) + [word]
                
        return list(count.values())
