```python
'''
# Maximum Subarray Sum with Non-Adjacent Jumps

# Difficulty: Hard

# Problem Description:
# You are given an array of integers `nums` representing values on a number line. You are initially positioned at index 0.
# You can jump forward from your current position `i` to either `i + 1` or `i + 2`.
# Find the maximum possible sum you can obtain by collecting the values at the indices you visit, with the additional constraint
# that you cannot visit adjacent indices in the array (except for the starting indices 0 and 1 if you choose to visit both).

# Examples:
# Example 1:
# Input: nums = [1, 2, 3, 1]
# Output: 4
# Explanation: You can collect 1 + 3 to get the maximum sum of 4.

# Example 2:
# Input: nums = [2, 7, 9, 3, 1]
# Output: 12
# Explanation: You can collect 2 + 9 + 1 to get the maximum sum of 12.

# Example 3:
# Input: nums = [1,2,3,4,5,6,7,8]
# Output: 16 
# Explanation: 1 + 3 + 5 + 7 = 16

# Constraints:
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
'''

class Solution:
    def maxNonAdjacentJumpSum(self, nums):
        """
        Calculates the maximum non-adjacent jump sum.

        Args:
            nums: The input array of integers.

        Returns:
            The maximum possible sum.
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        if n > 1:
            dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            # Case 1: Jump from i-1 and don't include i
            # Case 2: Jump from i-1, jump to i (valid only for n=2 or n=3)
            # Case 3: Jump from i-2 and include i
            # Case 4: Jump from i-2 and don't include i


            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            

        return dp[n-1]

# Test Cases
sol = Solution()
print(sol.maxNonAdjacentJumpSum([1, 2, 3, 1]))  # Output: 4
print(sol.maxNonAdjacentJumpSum([2, 7, 9, 3, 1]))  # Output: 12
print(sol.maxNonAdjacentJumpSum([1,2,3])) # Output: 3
print(sol.maxNonAdjacentJumpSum([1,2,3,4,5,6,7,8])) # Output: 16
print(sol.maxNonAdjacentJumpSum([1])) # Output: 1
print(sol.maxNonAdjacentJumpSum([])) # Output: 0




'''
Time Complexity: O(n) - We iterate through the `nums` array once.
Space Complexity: O(n) - We use a DP array of size n.  Could be optimized to O(1) by using only the previous two DP values.
'''
```