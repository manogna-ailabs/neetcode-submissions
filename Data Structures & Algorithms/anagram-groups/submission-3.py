class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # res = defaultdict(list)
        # for word in strs:
        #     count = [0]*26
        #     for c in word:
        #         count[ord(c)-ord('a')] += 1
        #     res[tuple(count)].append(word)
        # return list(res.values())

        maps = dict()
        for word in strs:
            sword = "".join(sorted(word))
            if sword not in maps:
                maps[sword] = []
            maps[sword].append(word)
        return list(maps.values())
            



