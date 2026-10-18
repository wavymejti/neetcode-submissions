class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dicto = {}
        record = 0
        l = 0
        for r in range(len(s)):
            if s[r] in dicto:
                dicto[s[r]] += 1
            else:
                dicto[s[r]] = 1
            while dicto[s[r]] > 1:
                dicto[s[l]] -= 1
                l += 1
            record = max(record, r - l + 1)
        return record
            