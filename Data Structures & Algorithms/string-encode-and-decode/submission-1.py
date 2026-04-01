class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ''
        for w in strs:
            out += str(len(w))+'#'+w
        return out

    def get_length(self,s):
        n = ''
        for ch in s:
            if ch != '#':
                n += ch
            else:
                break
        return n

    def decode(self, s: str) -> List[str]:
        strs = []
        while s!='':
            n = self.get_length(s)
            n_word, next_idx = int(n), len(n)+1 
            strs.append(s[next_idx:next_idx+n_word])
            s = s[next_idx+n_word:]
        return strs

