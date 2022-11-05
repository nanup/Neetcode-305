# https://leetcode.com/problems/minimum-window-substring/

# Given two strings s and t of lengths m and n respectively, 
# return the minimum window substring of s 
# such that every character in t (including duplicates) is included in the window. 
# If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

# Example 1:
    # Input: s = "ADOBECODEBANC", t = "ABC"
    # Output: "BANC"
    # Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

# Example 2:
    # Input: s = "a", t = "a"
    # Output: "a"
    # Explanation: The entire string s is the minimum window.

# Example 3:
    # Input: s = "a", t = "aa"
    # Output: ""
    # Explanation: Both 'a's from t must be included in the window.
    # Since the largest window of s only has one 'a', return empty string.

# Constraints:
    # m == s.length
    # n == t.length
    # 1 <= m, n <= 105
    # s and t consist of uppercase and lowercase English letters.

# Follow up: Could you find an algorithm that runs in O(m + n) time?

# Topic: Sliding Window
# First, make a charFreq dictionary of string t. Iterating through string s, if the char is found
# in charFreq, decrease the freq by 1. If the freq >= 0 (not == 0 to account for duplicates), 
# increase the matched count by 1. If matched count is equal to the length of string t
# unconditionally loop and adjust minLength, subArrayStart if needed. Also, if the leaving char
# is in charFreq, increase its frequency by 1 and if the frequency hits zero, one matched char is lost.

# Time Complexity: O(m + n)
# Space Complexity: O(m)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCharFreq = {}
        for char in t:
            tCharFreq[char] = 1 + tCharFreq.get(char, 0)

        minLength, start, subArrayStart = len(s) + 1, 0, 0
        matched = 0

        for end in range(len(s)):
            rightChar = s[end]

            if rightChar in tCharFreq:
                tCharFreq[rightChar] -= 1
            
                if tCharFreq[rightChar] >= 0:
                    matched += 1

            while matched == len(t):
                if minLength > end - start + 1:
                    minLength = end - start + 1
                    subArrayStart = start

                leftChar = s[start]
                start += 1

                if leftChar in tCharFreq:
                    if tCharFreq[leftChar] == 0:
                        matched -= 1
                    tCharFreq[leftChar] += 1

        if len(s) < minLength:
            return ""

        return s[subArrayStart:subArrayStart + minLength]