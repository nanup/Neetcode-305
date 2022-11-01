# https://leetcode.com/problems/reverse-linked-list/

# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Example 1:
    # Input: head = [1,2,3,4,5]
    # Output: [5,4,3,2,1]

# Example 2:
    # Input: head = [1,2]
    # Output: [2,1]

# Topic: LinkedList
# Three consecutive identifiers previous, head and next are carefully manipulated to reverse order

# Time Complexity: O(N)
# Space Complexity: O(1)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next

        return prev