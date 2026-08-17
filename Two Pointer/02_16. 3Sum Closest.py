class Solution(object):
    def threeSumClosest(self, nums, target):

        nums.sort()

        closest = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):

            left = i + 1
            right = len(nums) - 1

            while left < right:

                total = nums[i] + nums[left] + nums[right]

                # Check if current sum is closer
                if abs(total - target) < abs(closest - target):
                    closest = total

                # Exact answer
                if total == target:
                    return total

                # Need a bigger sum
                elif total < target:
                    left += 1

                # Need a smaller sum
                else:
                    right -= 1

        return closest

nums = [-1, 2, 1, -4]
target = 1

sol = Solution()

print(sol.threeSumClosest(nums, target))