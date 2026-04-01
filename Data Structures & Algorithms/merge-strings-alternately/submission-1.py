class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        i, j = 0, 0
        out = list(word1+word2)
        word1 = list(word1)
        word2 = list(word2)

        minL = min(m,n)
        out[0:minL*2:2] = word1[:minL]
        out[1:minL*2:2] = word2[:minL]
        if m == minL:
            out[minL*2:] =  word2[minL:]
        else:
            out[minL*2:] =  word1[minL:]
        return "".join(out)

