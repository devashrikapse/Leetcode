class Solution(object):
    def minSubArrayLen(self, target, nums):
        left = 0
        sum = 0
        min_len = float("inf")

        for right in range(len(nums)):
            sum += nums[right]

            while sum >= target:
                length = right - left + 1
                min_len = min(length, min_len)
                sum -= nums[left]
                left += 1

        if min_len == float('inf'):
            return 0

        return min_len

nums = [2,3,1,2,4,3]
solution = Solution()
print(solution.minSubArrayLen(7, nums))