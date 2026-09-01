class Solution:
    def splitArray(self, nums, k):
        left = max(nums)
        right = sum(nums)

        def canSplit(maxSum):
            parts = 1
            currentSum = 0

            for num in nums:
                if currentSum + num > maxSum:
                    parts += 1
                    currentSum = num
                else:
                    currentSum += num

            return parts <= k

        while left < right:
            mid = (left + right) // 2

            if canSplit(mid):
                right = mid
            else:
                left = mid + 1

        return left