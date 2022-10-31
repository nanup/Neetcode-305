# https://leetcode.com/problems/valid-palindrome/

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
# and removing all non-alphanumeric characters, it reads the same forward and backward. 
# Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:
    # Input: s = "A man, a plan, a canal: Panama"
    # Output: true
    # Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
    # Input: s = "race a car"
    # Output: false
    # Explanation: "raceacar" is not a palindrome.

# Constraints:
    # 1 <= s.length <= 2 * 105
    # s consists only of printable ASCII characters.


# Topic: Two Pointers
# After cleaning the string, two pointers, one from the start and other from the end
# can be used to compare characters and moved left to right and right to left correspondingly
# until they meet each other. Return True if the loop finishes without any inequality of characters
# at the position of each pointer

# Time Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # cleaning the string - O(N)
        s = s.translate(s.maketrans("", "", string.punctuation + " "))
        s = s.lower()

        # checking for palindrome - O(N)
        start, end = 0, len(s) - 1

        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1

        return True