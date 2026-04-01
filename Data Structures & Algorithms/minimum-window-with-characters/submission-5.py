class Solution:
    def check_counts(self, count_s, count_t):
        if len(count_s)<len(count_t):
            return False
        for ch, k in count_t.items():
            if count_s[ch] < k:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        if len(t) == 1:
            if t in s:
                return t
            else:
                return ""

        l = 0
        count_t = {}
        count_s = {}
        for ch in t:
            count_t[ch] = count_t.get(ch, 0) + 1
            count_s[ch] = 0

        minL = len(s)
        out = ""
        for r in range(len(s)):
            if s[r] in count_t:
                count_s[s[r]] = count_s.get(s[r], 0) + 1

            while s[l] not in count_t or count_s[s[l]]!=count_t[s[l]] and l<r:
                if s[l] in count_s:
                    count_s[s[l]] -= 1
                l += 1
            
            curr_count = self.check_counts(count_s, count_t)
            if curr_count:
                if r-l+1 <= minL:
                    minL=r-l+1
                    out = s[l:r+1]
                if s[l] in count_s:
                    count_s[s[l]] -= 1
                l += 1
        return out
