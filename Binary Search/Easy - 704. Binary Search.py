# https://leetcode.com/problems/binary-search/

# Given an array of integers nums which is sorted in ascending order, 
# and an integer target, write a function to search target in nums. 
# If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
    # Input: nums = [-1,0,3,5,9,12], target = 9
    # Output: 4
    # Explanation: 9 exists in nums and its index is 4

# Example 2:
    # Input: nums = [-1,0,3,5,9,12], target = 2
    # Output: -1
    # Explanation: 2 does not exist in nums so return -1

# Constraints:
    # 1 <= nums.length <= 104
    # -104 < nums[i], target < 104
    # All the integers in nums are unique.
    # nums is sorted in ascending order.
 
# Topic: Binary Search
# Since, the array is already sorted, binary search is preferable. Find the median index
# of the array and compare it to the target. If the target is bigger, it means target
# is to the right of median, else to the left of median. Adjust the size, find median 
# again for the new subarray and repeat until target and median are equal. If not found return -1.

# Time Complexity: O(logN)
# Space Complexity: O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        while start <= end:
            median = (end + start) // 2

            if target == nums[median]:
                return median
            elif target > nums[median]:
                start = median + 1
            else:
                end = median - 1

        return -1