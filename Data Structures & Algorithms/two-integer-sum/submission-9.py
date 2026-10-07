class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictonary = {}
        for i, num in enumerate(nums):
            newTarget = target - num
            if newTarget in dictonary:
                return [dictonary[newTarget], i]
            dictonary[num] = i