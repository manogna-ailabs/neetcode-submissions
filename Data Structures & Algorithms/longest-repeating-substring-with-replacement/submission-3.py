class Solution:
    def get_frequent_char(self, chars):
        frequent_char, frequent_char_count = "", 0
        for char, count in chars.items():
            if count>frequent_char_count:
                frequent_char, frequent_char_count = char, count
        
        return (frequent_char, frequent_char_count)

    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxL = 0
        chars = {}
        frequent_char, frequent_char_count = "", 0
        for r in range(len(s)):
            chars[s[r]] = chars.get(s[r], 0) + 1
            if chars[s[r]] > frequent_char_count:
                frequent_char = s[r]
                frequent_char_count = chars[s[r]]
            while (r - l + 1) - frequent_char_count>k:
                chars[s[l]] -= 1
                l += 1
            maxL = max(maxL, r-l+1)
        return maxL 
