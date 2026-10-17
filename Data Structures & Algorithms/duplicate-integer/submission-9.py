class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        widziane = set()
        for num in nums:
            if num in widziane:
                return True
            widziane.add(num)
        return False