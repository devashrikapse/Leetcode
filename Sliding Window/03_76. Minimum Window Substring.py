class Solution(object):
    def minWindow(self, s, t):

        # Frequency required from t
        need = {}

        for char in t:
            need[char] = need.get(char, 0) + 1

        window = {}

        left = 0

        formed = 0
        required = len(need)

        min_len = float('inf')
        min_start = 0

        for right in range(len(s)):

            char = s[right]

            # Add character to current window
            window[char] = window.get(char, 0) + 1

            # Required frequency has been satisfied
            if char in need and window[char] == need[char]:
                formed += 1

            # Window is valid → try shrinking
            while formed == required:

                # Update smallest window
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left

                # Remove left character
                left_char = s[left]
                window[left_char] -= 1

                # Window became invalid
                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1

                left += 1

        # No valid window
        if min_len == float('inf'):
            return ""

        return s[min_start:min_start + min_len]

s = "ADOBECODEBANC"
t = "ABC"

sol = Solution()

print(sol.minWindow(s, t))