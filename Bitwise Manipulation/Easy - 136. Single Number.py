# https://leetcode.com/problems/single-number/

# Given a non-empty array of integers nums, 
# every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Example 1:
    # Input: nums = [2,2,1]
    # Output: 1

# Example 2:
    # Input: nums = [4,1,2,1,2]
    # Output: 4

# Constraints:
    # 1 <= nums.length <= 3 * 104
    # -3 * 104 <= nums[i] <= 3 * 104
    # Each element in the array appears twice except for one element which appears only once.

# Topic: Bitwise Manipulation
# When number is xorred to itself it becomes zero. So, if we XOR all the numbers in the list
# only the single element will be finally xorred with zero which will always result in the same
# element. That single element will be the element which has only one count.

# TIme Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = 0
        for num in nums:
            n ^= num

        return n