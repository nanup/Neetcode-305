# https://leetcode.com/problems/two-sum/

# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:
    # Input: nums = [2,7,11,15], target = 9
    # Output: [0,1]
    # Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
    # Input: nums = [3,2,4], target = 6
    # Output: [1,2]

# Constraints:
    # 2 <= nums.length <= 104
    # -109 <= nums[i] <= 109
    # -109 <= target <= 109
    # Only one valid answer exists.

# Topic: Hashing
# A dictionary is created. For each num in nums, if (target - nums[i]) is not present in dictionary
# the num and its index is stored. Else, the pair is found and returned.

# Time Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}

        for i in range(len(nums)):
            if target - nums[i] not in dict:
                dict[nums[i]] = i
            else:
                return[i, dict[target - nums[i]]]