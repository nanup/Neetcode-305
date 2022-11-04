# https://leetcode.com/problems/permutation-in-string/

# Given two strings s1 and s2, return true 
# if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

# Example 1:
    # Input: s1 = "ab", s2 = "eidbaooo"
    # Output: true
    # Explanation: s2 contains one permutation of s1 ("ba").

# Example 2:
    # Input: s1 = "ab", s2 = "eidboaoo"
    # Output: false

# Constraints:
    # 1 <= s1.length, s2.length <= 104
    # s1 and s2 consist of lowercase English letters.

# Topic: Sliding Window
# Use a dict to maintain track of the frequency of numbers and a variable for number of matched
# characters.

# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict = {}
        count = 0

        for char in s1:
            dict[char] = 1 + dict.get(char, 0)

        start = 0

        for end in range(len(s2)):
            rightChar = s2[end]

            if rightChar in dict:
                dict[rightChar] -= 1

                if dict[rightChar] == 0:
                    count += 1

            if count == len(dict):
                return True

            if end - start + 1 > k:
                leftChar = s2[left]
                if leftChar in dict:
                    if dict[leftChar] == 0:
                        count -= 1
                    dict[leftChar] += 1
                left += 1

        return False