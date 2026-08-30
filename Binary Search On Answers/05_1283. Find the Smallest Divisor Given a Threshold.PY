class Solution(object):
    def smallestDivisor(self, nums, threshold):

        left = 1
        right = max(nums)

        answer = right

        while left <= right:

            divisor = (left + right) // 2

            total = 0

            for num in nums:
                total += (num + divisor - 1) // divisor

            if total <= threshold:
                # Divisor works, try smaller
                answer = divisor
                right = divisor - 1

            else:
                # Divisor is too small
                left = divisor + 1

        return answer