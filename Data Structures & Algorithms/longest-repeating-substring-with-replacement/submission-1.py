class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, n = 0, len(s)
        res = 0
        freq = [0] * 26

        for r in range(n):
            freq[self.c_to_i(s[r])] += 1
            while (r - l + 1) - max(freq) > k:
                freq[self.c_to_i(s[l])] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res


    def c_to_i(self, c: char) -> int:
        return ord(c) - 65