class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for liczba in counter:
            if counter[liczba] == 1:
                return liczba