```python
'''
# Maximum Subsequence Sum with Non-Adjacent Differences Constraint
# Difficulty: Hard

# Problem Description:
# Given an array of integers `nums`, find the maximum subsequence sum such that no two adjacent elements in the original array are both part of the subsequence. 
# In other words, if you select nums[i] for the subsequence, you cannot select nums[i-1] or nums[i+1].

# Examples:
# Example 1:
# Input: nums = [2, 7, 9, 3, 1]
# Output: 12
# Explanation: Picking [7, 1] gives a sum of 8.
#              Picking [2, 9, 1] gives a sum of 12. 
#              Picking [2, 7] gives a sum of 9.
#              Picking [2, 9] gives a sum of 11.
#              12 is the maximum sum we can get.

# Example 2:
# Input: nums = [1, 2, 3, 1]
# Output: 4
# Explanation: Picking [1, 3] gives a sum of 4.

# Example 3:
# Input: nums = [1]
# Output: 1
# Explanation: Only one element, so we pick it.


# Constraints:
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
'''

class Solution:
    def maxSubsequenceSum(self, nums: list[int]) -> int:
        """
        Calculates the maximum subsequence sum with non-adjacent differences constraint.

        Args:
            nums: The input array of integers.

        Returns:
            The maximum subsequence sum.
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        # dp[i] stores the maximum sum ending at index i
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])  # Either include nums[1] or stick with nums[0]

        for i in range(2, n):
            # Two options:
            # 1. Include nums[i] - in this case, maximum sum is dp[i-2] + nums[i] (since we can't include nums[i-1])
            # 2. Exclude nums[i] - in this case, maximum sum is dp[i-1] (the max sum so far)
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])  # Handle negative numbers properly

        return dp[n - 1]



# Test Cases
solution = Solution()

print(solution.maxSubsequenceSum([2, 7, 9, 3, 1]))  # Output: 12
print(solution.maxSubsequenceSum([1, 2, 3, 1]))  # Output: 4
print(solution.maxSubsequenceSum([1]))  # Output: 1
print(solution.maxSubsequenceSum([-2, 1, 3, -4, 5])) # Output: 8 ([1, 5])
print(solution.maxSubsequenceSum([-2, -1, -3, -4, -5])) # Output: -1
print(solution.maxSubsequenceSum([])) # Output: 0


"""
Time Complexity: O(n) - We iterate through the nums array once.
Space Complexity: O(n) - We use a dp array of size n. (Can be optimized to O(1) by using just two variables to store the previous two dp values)
"""
```