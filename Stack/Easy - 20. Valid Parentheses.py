# https://leetcode.com/problems/valid-parentheses/

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.

# An input string is valid if:
    # Open brackets must be closed by the same type of brackets.
    # Open brackets must be closed in the correct order.
    # Every close bracket has a corresponding open bracket of the same type.

# Example 1:
    # Input: s = "()"
    # Output: true

# Example 2:
    # Input: s = "()[]{}"
    # Output: true

# Constraints:
    # 1 <= s.length <= 104
    # s consists of parentheses only '()[]{}'.

# Topic: Stack
# Iterating through the string each open bracket is stored on a stack. When a closed bracket is
# encountered, the stack is popped and a check is done if the brackets are of the same type.
# If all of the iterations complete and no elements are left in stack, return True.

# Time Complexity: O(N)
# Space Complexity: O(N)
from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        brackets = {"(":")", "{":"}", "[":"]"}
        
        for bracket in s:
            if bracket in brackets:
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False

                openBrkt = stack.pop()

                if brackets[openBrkt] != bracket:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False