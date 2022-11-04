# https://leetcode.com/problems/longest-repeating-character-replacement/

# You are given a string s and an integer k. You can choose any character of the string 
# and change it to any other uppercase English character. 
# You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter 
# you can get after performing the above operations.

# Example 1:
    # Input: s =  "ABAB", k = 2
    # Output: 4
    # Explanation: Replace the two 'A's with two 'B's or vice versa.

# Example 2:
    # Input: s = "AABABBA", k = 1
    # Output: 4
    # Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
    # The substring "BBBB" has the longest repeating letters, which is 4.

# Constraints:
    # 1 <= s.length <= 105
    # s consists of only uppercase English letters.
    # 0 <= k <= s.length

# Topic: Sliding Window
# Store the frequency of chars in a dictionary. Maintain a variable with the max occurence of
# the char. When a new char is overtakes the max occurence, replace the max occurence. If the diff
# of max occurence and length of subarray is greater than k, move the left pointer ahead by one
# and also decrease its frequency by one.

# Time Complexity: O(N)
# Space Complexity; O(N)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        left, right = 0, 0
        maxCount, result = 0, 0

        while end < len(s):
            seen[s[right]] = 1 + seen.get(s[right], 0)
            maxCount = max(maxCount, seen[s[right]])

            if right - left + 1 - maxCount > k:
                seen[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)
            end += 1

        return result