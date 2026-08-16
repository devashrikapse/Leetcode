class Solution(object):
    def characterReplacement(self, s, k):

        count = {}

        left = 0
        max_freq = 0
        max_len = 0

        for right in range(len(s)):

            # Add current character
            count[s[right]] = count.get(s[right], 0) + 1

            # Highest frequency character in window
            max_freq = max(max_freq, count[s[right]])

            # Characters that need replacement
            window_len = right - left + 1
            replacements = window_len - max_freq

            # Window is invalid
            while replacements > k:

                count[s[left]] -= 1
                left += 1

                window_len = right - left + 1
                replacements = window_len - max_freq

            # Update answer
            max_len = max(max_len, right - left + 1)

        return max_len
s = "AABABBA"
k = 1

sol = Solution()

print(sol.characterReplacement(s, k))