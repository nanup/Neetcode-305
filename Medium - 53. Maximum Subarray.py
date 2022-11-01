# https://leetcode.com/problems/maximum-subarray/

# Given an integer array nums, find the subarray which has the largest sum and return its sum.

# Example 1:
    # Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    # Output: 6
    # Explanation: [4,-1,2,1] has the largest sum = 6.

# Example 2:
    # Input: nums = [1]
    # Output: 1

# Constraints:
    # 1 <= nums.length <= 105
    # -104 <= nums[i] <= 104

# Follow up: If you have figured out the O(n) solution, 
# try coding another solution using the divide and conquer approach, which is more subtle.

# Topic: Sliding Window
# In this modified sliding window, if the num at windowStart is not positive, it effectively has
# no contribution to the sum and can be ignored (reset to zero). windowEnd moves ahead and in
# each iteration maxSum is calculated. maxSum needs to be initialized to the first num in the list\
# to make sure even lists with all negative elements have a maxSum other than zero.

# Time Complexity: O(N)
# Space Complexity: O(1)
import math

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        end, currSum = 0, 0

        while end < len(nums):
            currSum += nums[end]
            maxSum = max(currSum, maxSum)

            if currSum < 0:
                currSum = 0
            
            end += 1

        return maxSum