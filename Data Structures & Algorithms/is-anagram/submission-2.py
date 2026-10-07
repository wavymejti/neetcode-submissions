class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        counters = {}
        for k in s:
            if k in counters:
                counters[k] += 1
            else:
                counters[k] = 1

        
        countert = {}
        for k in t:
            if k in countert:
                countert[k] += 1
            else:
                countert[k] = 1
        
        if counters == countert:
            return True
        else:
            return False