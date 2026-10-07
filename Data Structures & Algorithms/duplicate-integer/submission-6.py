class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
    
        counter = {}
        for n in nums:
            if n in counter:
                counter[n] += 1
            else:
                counter[n] = 1
        
        for k in counter.values():
            if k > 1:
                return True
        return False