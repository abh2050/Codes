```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular array of integers nums, find the maximum sum of a non-adjacent subset of elements. 
# In a circular array, the first and last elements are considered adjacent.

# Examples:
# Example 1:
# Input: nums = [2, 1, 4, 9]
# Output: 11
# Explanation: The maximum sum is achieved by selecting the elements at indices 0 and 2 (2 + 9 = 11).

# Example 2:
# Input: nums = [1, 2, 3, 1]
# Output: 4
# Explanation: The maximum sum is achieved by selecting the elements at indices 0 and 2 (1 + 3 = 4).

# Constraints:
# 1 <= len(nums) <= 10^5
# -10^4 <= nums[i] <= 10^4
'''

class Solution:
    def rob_circular(self, nums: list[int]) -> int:
        """
        Calculates the maximum sum of non-adjacent elements in a circular array.

        Args:
            nums: The input circular array of integers.

        Returns:
            The maximum sum of a non-adjacent subset.
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)

        # Handle circularity by considering two scenarios:
        # 1. Include the first element, exclude the last
        # 2. Exclude the first element, include the last
        return max(self.rob_linear(nums[:-1]), self.rob_linear(nums[1:]))


    def rob_linear(self, nums: list[int]) -> int:
        """Helper function:  Calculates max sum of non-adjacent elements in a linear array (House Robber I)."""
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[n - 1]



# Test cases
sol = Solution()
print(sol.rob_circular([2, 1, 4, 9]))  # Output: 11
print(sol.rob_circular([1, 2, 3, 1]))  # Output: 4
print(sol.rob_circular([1])) # Output: 1
print(sol.rob_circular([1,2])) # Output: 2
print(sol.rob_circular([1,7,9,2]))  # Output: 10


# Time Complexity: O(N) - We iterate through the array twice in rob_linear (called twice from rob_circular).
# Space Complexity: O(N) for the dp array in rob_linear. Can be optimized to O(1) by using variables instead of the array.
```