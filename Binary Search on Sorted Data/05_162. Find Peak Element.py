class Solution(object):
    def findPeakElement(self, nums):

        left = 0
        right = len(nums) - 1

        while left < right:

            mid = (left + right) // 2

            if nums[mid] < nums[mid + 1]:
                # We are going uphill
                left = mid + 1
            else:
                # We are going downhill
                right = mid

        return left