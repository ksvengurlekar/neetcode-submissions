from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for s in strs:
            key = self.stringify(s)
            if key in hm:
                hm[key].append(s)
            else:
                hm[key] = [s]

        return [hm[x] for x in hm]
    
    def stringify(self, s: str) -> str:
        res = ""
        freq = Counter(s.lower())
        for i in range(ord('a'), ord('z')+1):
            res += chr(i) + str(freq[chr(i)])

        return res
        
        