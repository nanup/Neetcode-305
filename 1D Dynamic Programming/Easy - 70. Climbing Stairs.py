# https://leetcode.com/problems/climbing-stairs/

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways 
# can you climb to the top?

# Example 1:
    # Input: n = 2
    # Output : 2
    # Explanation: There are two ways to climb to the top.
    # 1. 1 step + 1 step
    # 2. 2 steps

# Example 2:
    # Input: n = 3
    # Output: 3
    # Explanation: There are three ways to climb to the top.
    # 1. 1 step + 1 step + 1 step
    # 2. 1 step + 2 steps
    # 3. 2 steps + 1 step

# Constraints:
    # 1 <= n <= 45

# Topic: Dynamic Programming
# The number of ways of reaching a step is the sum of the number of ways of reaching the step before
# it and the number of ways of reaching the step twice before it. So, it is similar to Fibonacci
# series and so two variables are added, and moved forward. One takes the value of the sum and the
# other takes the value of the one who moved ahead. Base case is when n <= 3 when the number of steps
# is same as n.

# Time Complexity: O(N)
# Space Complexity: O(1)

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n

        n1, n2 = 2, 3

        for i in range(4, n + 1):
            temp = n1 + n2
            n1 = n2
            n2 = temp

        return n2