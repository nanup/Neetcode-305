# https://leetcode.com/problems/trapping-rain-water/

# Given n non-negative integers representing an elevation map where 
# the width of each bar is 1, compute how much water it can trap after raining.

# Example 1:
    # Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
    # Output: 6
    # Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

# Example 2:
    # Input: height = [4,2,0,3,2,5]
    # Output: 9

# Constraints:
    # n == height.length
    # 1 <= n <= 2 * 104
    # 0 <= height[i] <= 105

# Topic: Two Pointers
# Start two pointers, one at the beginning and the other at the end of height list. Depending on
# which one is higher modify the pointer by 1. For the new height encountered after find if its
# higher than before. Subtracting the new height max will give the area it offers, if its the highest
# there is no area offerd and it becomes the new max height of that direction. Keep adding
# all the areas to a variable and return that.

# Time Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]

        while left < right:
            if height[left] >= height[right]:
                right -= 1
                rightMax = max(height[right], rightMax)
                result += rightMax - height[right]
            else:
                left += 1
                leftMax = max(height[left], leftMax)
                result += leftMax - height[left]

        return result