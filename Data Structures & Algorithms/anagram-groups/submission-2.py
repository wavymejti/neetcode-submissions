class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26 #for a ... z
            
            for c in s:
                count[ord(c) - ord("a")] += 1 # thanks to - ord(a) we have waypoint that always wull get us right numbers 
            res[tuple(count)].append(s)
        return list(res.values())
