# https://leetcode.com/problems/product-of-array-except-self/

# Given an integer array nums, return an array answer such that answer[i] 
# is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:
    # Input: nums = [1,2,3,4]
    # Output: [24,12,8,6]

# Example 2:
    # Input: nums = [-1,1,0,-3,3]
    # Output: [0,0,9,0,0]

# Constraints:
    # 2 <= nums.length <= 105
    # -30 <= nums[i] <= 30
    # The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# Topic: Precomputation
# Form two arrays, one prefix product array and another suffix product array.
# Product of elements of the same index in both arrays gives the result.

# Time Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        prefix, suffix = 1, 1 # prefix carries the value of prefix product until that index

        for i in range(len(nums)):
            result[i] *= prefix
            prefix *= nums[i] # next element is multiplied into the prefix
            result[len(nums) - i - 1] *= suffix
            suffix *= nums[len(nums) - i - 1] # previous element is multiplied into the suffix

        return result
