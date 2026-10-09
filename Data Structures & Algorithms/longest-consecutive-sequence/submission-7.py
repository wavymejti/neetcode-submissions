class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #zliczanie i przechowywanie w slowniku
        zbiorwystapien = set(nums)
        longest = 0
        for num in zbiorwystapien:
            if num - 1 in zbiorwystapien:
                continue
            length = 1
            while num + 1 in zbiorwystapien:
                length += 1
                num += 1
            longest = max(longest, length)
        return longest

