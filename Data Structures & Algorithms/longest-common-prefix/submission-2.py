class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        out = ""
        n = len(strs)
        if n == 1:
            return strs[0]
        
        minl = len(strs[0])
        ref = strs[0]
        for i, word in enumerate(strs):
            if len(word) < minl:
                ref = word
                minl = len(word)

        for i in range(minl):
            ch = ref[i]
            flag = True
            for word in strs:
                if len(word)==0:
                    return ""
                elif ch != word[i]:
                    flag = False
                    break
            if flag:
                out += ch
            else:
                break
        return out
