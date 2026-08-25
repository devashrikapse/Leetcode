class Solution(object):
    def shipWithinDays(self, weights, days):

        left = max(weights)
        right = sum(weights)

        answer = right

        while left <= right:

            capacity = (left + right) // 2

            current_weight = 0
            days_needed = 1

            for weight in weights:

                if current_weight + weight > capacity:
                    days_needed += 1
                    current_weight = weight
                else:
                    current_weight += weight

            if days_needed <= days:
                # Capacity works, try smaller
                answer = capacity
                right = capacity - 1

            else:
                # Capacity is too small
                left = capacity + 1

        return answer