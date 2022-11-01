# https://leetcode.com/problems/valid-anagram/

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.

# Example 1:
    # Input: s = "anagram", t = "nagaram"
    # Output: true

# Example 2:
    # Input: s = "rat", t = "car"
    # Output: false

# Constraints:
    # 1 <= s.length, t.length <= 5 * 104
    # s and t consist of lowercase English letters.

# Follow up: What if the inputs contain Unicode characters? 
# How would you adapt your solution to such a case?

# Topic: Hashing
# Store all the letters in s in a dict. Iterate through s and check if the letter and its frequency
# isn't invalid.

# Time Complexity: O(N + K)
# Space Complexity: O(K)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letterFreq = {}

        for letter in s:
            if letter not in letterFreq:
                letterFreq[letter] = 0
            letterFreq[letter] += 1

        for letter in t:
            if letter not in letterFreq:
                return False

            if letterFreq[letter] < 1:
                return False

            letterFreq[letter] -= 1

        return True