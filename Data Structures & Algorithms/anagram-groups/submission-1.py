from collections import Counter 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anas = {}
        for s in strs:
            key = self.hashs(s)
            if key in anas:
                anas[key].append(s)
            else:
                anas[key] = [s]
        
        return [anas[v] for v in anas]

    def hashs(self, s: str) -> str:
        res = ""
        freq = Counter(s.lower())
        for i in range(ord('a'), ord('z')+1):
            res += chr(i) + str(freq[chr(i)])

        return res
