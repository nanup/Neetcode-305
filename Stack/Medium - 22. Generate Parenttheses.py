# https://leetcode.com/problems/generate-parentheses/

# Given n pairs of parentheses, write a function to 
# generate all combinations of well-formed parentheses.

# Example 1:
    # Input: n = 3
    # Output: ["((()))","(()())","(())()","()(())","()()()"]

# Example 2:
    # Input: n = 1
    # Output: ["()"]

# Constraints:
    # 1 <= n <= 8

# Topic: Stack
# A breadth first search of a queue is implemented. Starting with an empty string, open brace 
# and closed brace count are tracked. When both of them become equal to n, the string is appended
# to the result. If open count is less than n append an open brace. If closed count is less than
# open count and open count is not zero, append a closed brace.

# Time Complexity: O(N)
# Space Complexity: O(N)
from collections import deque

class Solution:
    def generateParenthesis(self, n):
        result = []
        queue = deque()
        # [string, openCount, closedCount]
        queue.append(["", 0, 0])
        while queue:
            levelSize = len(queue)
            print(queue)
            for i in range(levelSize):
                curr = queue.popleft()
                currString = curr[0]
                openCount, closedCount = curr[1], curr[2]
                if openCount == n and closedCount == n:
                    result.append(currString)
                else:
                    if openCount < n:
                        currString = curr[0]
                        currString += "("
                        queue.append([currString, openCount + 1, closedCount])
                    if openCount > 0 and closedCount < openCount:
                        currString = curr[0]
                        currString += ")"
                        queue.append([currString, openCount, closedCount + 1])
        return result

sol = Solution()
print(sol.generateParenthesis(3))