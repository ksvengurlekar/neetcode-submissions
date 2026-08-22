from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = Counter(nums)
        buckets = [[] for _ in range(len(nums))]

        for value, count in hashmap.items():
            buckets[count-1].append(value)

        result = []
        for l in buckets[::-1]:
            for i in l:
                if k > 0:
                    result.append(i)
                    k -= 1
                else:
                    break

        return result
