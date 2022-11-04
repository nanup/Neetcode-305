# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
    # Input: s = "abcabcbb"
    # Output: 3
    # Explanation: The answer is "abc", with the length of 3.

# Example 2:
    # Input: s = "bbbbb"
    # Output: 1
    # Explanation: The answer is "b", with the length of 1.

# Example 3:
    # Input: s = "pwwkew"
    # Output: 3
    # Explanation: The answer is "wke", with the length of 3.
    # Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Constraints:
    # 0 <= s.length <= 5 * 104
    # s consists of English letters, digits, symbols and spaces.

# Topic: Sliding Window
# A dictionary or a deque can be maintained to track the numbers seen

# Time Complexity: O(N)
# Space Complexity: O(N)
from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # subString = deque()

        # start, end = 0, 0

        # result = 0

        # while end < len(s):
        #     char = s[end]

        #     while char in subString:
        #         subString.popleft()
        #     subString.append(char)

        #     result = max(result, len(subString))

        # return result

# ------------------- algorithm #2 ------------------------
        seen = {}

        left, right = 0, 0

        longest = 0

        while right < len(s):
            char = s[end]

            if char in seen:
                left = max(left, seen[char] + 1)
            longest = max(longest, right - left + 1)

            seen[right] = right

            right += 1

        return longest
