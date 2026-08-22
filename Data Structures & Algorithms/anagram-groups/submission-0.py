class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = {} # set -> list of scambles
        for s in strs:
            scramble = ''.join(sorted(s))
            if scramble in mapping:
                mapping[scramble].append(s)
            else:
                mapping[scramble] = [s]
            
        return mapping.values()
            
        