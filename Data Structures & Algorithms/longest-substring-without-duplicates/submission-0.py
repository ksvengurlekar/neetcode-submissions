class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, n = 0, len(s)
        window = set()
        maxwindow = 0
        for r in range(n):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            
            window.add(s[r])
            maxwindow = max(maxwindow, len(window))

        return maxwindow