# https://leetcode.com/problems/invert-binary-tree/

# Given the root of a binary tree, invert the tree, and return its root.

# Example 1:
    # Input: root = [4,2,7,1,3,6,9]
    # Output: [4,7,2,9,6,3,1]

# Example 2:
    # Input: root = [2,1,3]
    # Output: [2,3,1]

# Constraints:
    # The number of nodes in the tree is in the range [0, 100].
    # -100 <= Node.val <= 100

# Topic: Trees
# A stack is used to maintain a list of nodes in one level. The branches are swapped
# and these branch nodes are added to the stack. Repeated until the stack is empty.

# Time Complexity: O(N)
# Space Complexity: O(N)
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = deque()
        stack.append(root)

        while stack:
            currNode = stack.pop()

            if currNode:
                currNode.left, currNode.right = currNode.right, currNode.left
                stack.append(currNode.left)
                stack.append(currNode.right)

        return root