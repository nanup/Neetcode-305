# https://leetcode.com/problems/contains-duplicate/

# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.

# Example 1:
    # Input: nums = [1,2,3,1]
    # Output: true

# Example 2:
    # Input: nums = [1,2,3,4]
    # Output: false

# Constraints:
    # 1 <= nums.length <= 105
    # -109 <= nums[i] <= 109

# Topic: Hashing
# nums is iterated to store each num in a dictionary
# If in any iteration, a value is found to be > 1, returns true, else false

# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numFreq = {}

        for i in range(len(nums)):
            num = nums[i]
            
            if num not in numFreq:
                numFreq[num] = 0
            numFreq[num] += 1

            if numFreq[num] > 1:
                return True
        
        return False

# Topic: Sorting
# nums is sorted and iterated to check if any two consecutive terms are the same

# Time Complexity: O(N * logN)
# Space Complexity: O(1)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                return True
        
        return False