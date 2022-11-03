# https://leetcode.com/problems/top-k-frequent-elements/

# Given an integer array nums and an integer k, return the k most frequent elements. 
# You may return the answer in any order.

# Example 1:
    # Input: nums = [1,1,1,2,2,3], k = 2
    # Output: [1,2]

# Example 2:
    # Input: nums = [1], k = 1
    # Output: [1]

# Constraints:
    # 1 <= nums.length <= 105
    # -104 <= nums[i] <= 104
    # k is in the range [1, the number of unique elements in the array].
    # It is guaranteed that the answer is unique.

# Follow up: Your algorithm's time complexity must be better than O(n log n), 
# where n is the array's size.

# Topic: Heap
# Using a minHeap store the frequncies and the corresponding numbers in a tuple. Pop elements 
# if they are greater than k in number and finally only k max frequent elements are left out. 

# Time Complexity: O(N * logN)
# Space Complexity: O(N)
from heapq import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minHeap = []

        numFreq = {}

        for num in nums:
            if num not in numFreq:
                numFreq[num] = 0
            numFreq[num] += 1

        for items in numFreq.items():
            heappush(minHeap, (-items[1], items[0]))
            if len(minHeap) > k:
                heappop(minHeap)

        return [item[1] for item in minHeap]