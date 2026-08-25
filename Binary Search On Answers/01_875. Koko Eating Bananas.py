class Solution(object):
    def minEatingSpeed(self, piles, h):

        left = 1
        right = max(piles)

        answer = right

        while left <= right:

            k = (left + right) // 2

            hours = 0

            for pile in piles:
                hours += (pile + k - 1) // k

            if hours <= h:
                # k works, try a smaller speed
                answer = k
                right = k - 1

            else:
                # k is too slow
                left = k + 1

        return answer