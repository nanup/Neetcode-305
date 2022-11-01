# https://leetcode.com/problems/ransom-note/

# Given two strings ransomNote and magazine, return true 
# if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

# Example 1:
    # Input: ransomNote = "a", magazine = "b"
    # Output: false

# Example 2:
    # Input: ransomNote = "aa", magazine = "ab"
    # Output: false

# Constraints:
    # 1 <= ransomNote.length, magazine.length <= 105
    # ransomNote and magazine consist of lowercase English letters.

# Topic: Hashing
# First add the letters with their frequencies to a dict. Then, iterate through the ransomNote
# and check if the frequency of that letter in dict is greater than zero until all iterations are done.

# Time Complexity: O(N + K)
# Space Complexity: O(K)
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letterFreq = {}

        for letter in magazine:
            if letter not in letterFreq:
                letterFreq[letter] = 0
            letterFreq[letter] += 1

        for letter in ransomNote:
            if letter not in letterFreq:
                return False

            if letterFreq[letter] < 1:
                return False

            letterFreq[letter] -= 1

        return True