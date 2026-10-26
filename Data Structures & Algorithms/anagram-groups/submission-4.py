from collections import Counter

class AlphaMap:
    def __init__(self, counts):
        self.alpha = ["0"] * 26
        for element, count in counts.items():
            self.alpha[ord(element) - ord('a')] = str(count)

    def hashup(self):
        return "-".join(self.alpha)


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:

            x = AlphaMap(Counter(s)).hashup()
            if x not in groups.keys():
                groups[x] = [s]
            else:
                groups[x].append(s)

        return list(groups.values())