# https://leetcode.com/problems/sliding-window-maximum/

# You are given an array of integers nums, there is a sliding window of size k 
# which is moving from the very left of the array to the very right. 
# You can only see the k numbers in the window. 
# Each time the sliding window moves right by one position.

# Return the max sliding window.

# Example 1:
    # Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
    # Output: [3,3,5,5,6,7]
    # Explanation: 
    # Window position                Max
    # ---------------               -----
    # [1  3  -1] -3  5  3  6  7       3
    #  1 [3  -1  -3] 5  3  6  7       3
    #  1  3 [-1  -3  5] 3  6  7       5
    #  1  3  -1 [-3  5  3] 6  7       5
    #  1  3  -1  -3 [5  3  6] 7       6
    #  1  3  -1  -3  5 [3  6  7]      7

# Example 2:
    # Input: nums = [1], k = 1
    # Output: [1]

# Constraints:
    # 1 <= nums.length <= 105
    # -104 <= nums[i] <= 104
    # 1 <= k <= nums.length

# Topic: Sliding Window
# We can make a montonic decreasing stack with the maximum of the elements visible to us in each
# iteration. If a new element is greater than the elements in queue from right to left, pop them
# until the new element is the smallest in the queue. This ensures only the maximum's of each
# window are stored and rest are discarded. When the window is moving foward, pop the max queue[0]
# if it is the element leaving the window.

# Time Complexity: O(N)
# Space Complexity: O(k)
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []

        start, end = 0, 0

        queue = deque()

        while end < len(nums):
            while queue and nums[end] > queue[-1]:
                queue.pop()
            queue.append(nums[end])

            if end - start + 1 == k:
                result.append(queue[0])

                if nums[start] == queue[0]:
                    queue.popleft()
                start += 1

            end += 1

        return result