class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}          # char -> latest index
        left = 0
        longest_len = 0

        for right, char in enumerate(s):

            # duplicate inside current window
            if char in seen and seen[char] >= left:
                left = seen[char] + 1

            seen[char] = right

            current_len = right - left + 1
            longest_len = max(longest_len, current_len)

        return longest_len