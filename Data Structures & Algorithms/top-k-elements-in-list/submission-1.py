class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dictonary = {}
        for num in nums:
            if num not in dictonary:
                dictonary[num] = 1
            else:
                dictonary[num] += 1
        
        ranking = sorted(dictonary, key=dictonary.get, reverse=True)
        return ranking[:k]