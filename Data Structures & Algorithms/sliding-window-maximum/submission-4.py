from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        result = []

        for i in range(len(nums)):
            # choose bring a max to front
            while q and nums[i] > nums[q[-1]]:
                q.pop()

            # always add newly considered value
            q.append(i)

            # check if value is a max at the end of window
            if i >= k-1:
                result.append(nums[q[0]])

            # value is out of window
            if q[0] <= i+1-k:
                q.popleft()

        return result