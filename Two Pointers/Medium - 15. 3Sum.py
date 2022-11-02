# https://leetcode.com/problems/3sum/

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Example 1:
    # Input: nums = [-1,0,1,2,-1,-4]
    # Output: [[-1,-1,2],[-1,0,1]]
    # Explanation: 
        # nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
        # nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
        # nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
        # The distinct triplets are [-1,0,1] and [-1,-1,2].
        # Notice that the order of the output and the order of the triplets does not matter.

# Example 2:
    # Input: nums = [0,1,1]
    # Output: []
    # Explanation: The only possible triplet does not sum up to 0.

# Example 3:
    # Input: nums = [0,0,0]
    # Output: [[0,0,0]]
    # Explanation: The only possible triplet sums up to 0.

# Constraints:
    # 3 <= nums.length <= 3000
    # -105 <= nums[i] <= 105

# Topic: Two Pointers
# Sort the array first to be able to use pointers sequentially. For each element in the array
# create two pointers, one starting one ahead of element and the other at the end of array.
# Find sum of all three and append to result if it is zero. Skip elements if they are duplicates
# of previous elements by increasing or decreasing their pointers. If the sum is greater than or
# lesser than zero modify the pointer accordingly and loop until both pointers meet.

# Time Complexity: O(N^2)
# Space Complexity: O(N)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []

        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                currSum = nums[i] + nums[j] + nums[k]

                if currSum == 0:
                    triplets.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    while j > i + 1 and nums[j - 1] == nums[j]:
                        j += 1
                
                    while k < len(nums) - 1 and nums[k + 1] == nums[k]:
                        k -= 1
                elif currSum > 0:
                    k -= 1
                else:
                    j += 1

        return triplets