class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        best = r

        while l <= r:
            k = l + (r - l)//2

            s = 0
            for p in piles:
                s += math.ceil(float(p) / k)
            
            if s <= h:
                r = k - 1
                best = k
            else:
                l = k + 1
                
        
        return best