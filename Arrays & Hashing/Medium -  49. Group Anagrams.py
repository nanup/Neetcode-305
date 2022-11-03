# https://leetcode.com/problems/group-anagrams/

# Given an array of strings strs, group the anagrams together. 
# You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

# Example 1:
    # Input: strs = ["eat","tea","tan","ate","nat","bat"]
    # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:
    # Input: strs = [""]
    # Output: [[""]]

# Example 3:
    # Input: strs = ["a"]
    # Output: [["a"]]

# Constraints:
    # 1 <= strs.length <= 104
    # 0 <= strs[i].length <= 100
    # strs[i] consists of lowercase English letters.

# Topic: Hashing
# We note that there are only 26 lowercase letters and so can be implemented as a 26 length list.
# Two letters which are anagrams will have the same 26 length list and if they are same, we can
# append the string to the list which is stored as a key in a dictionary. All anagrams go to
# the same key 26 length count list.

# Time Complexity: O(m * N)
# Space Complexity: O(N)
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) # defaultdict returns the result of its argument if key is not found

        for str in strs:
            count = [0] * 26

            for char in str:
                count[ord(char) - ord("a")] += 1
            result[tuple(count)].append(str)
            # if a match is found in result dict, the key is the same count as now
            # since python cant use list as an index for dict we turn it into tuple

        return result.values()