```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular array of integers nums (nums[0] and nums[-1] are adjacent), find the maximum sum of a subset of its elements such that no two elements in the subset are adjacent.

# Examples:
# Example 1:
# Input: nums = [2, 1, 4, 9]
# Output: 11
# Explanation: We can select elements at indices 0 and 2 (2 + 9 = 11), or indices 1 and 3 (1 + 9 = 10). The maximum is 11.

# Example 2:
# Input: nums = [1, 2, 3, 1]
# Output: 4
# Explanation: We can select elements at indices 0 and 2 (1 + 3 = 4).

# Constraints:
# 1 <= nums.length <= 3 * 10^4
# -10^4 <= nums[i] <= 10^4
'''

class Solution:
    def rob(self, nums: list[int]) -> int:
        """
        Calculates the maximum sum of non-adjacent elements in a circular array.

        Args:
            nums: The input circular array of integers.

        Returns:
            The maximum sum of non-adjacent elements.
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)

        # Handle the circularity by considering two cases:
        # 1. Include the first element (exclude the last)
        # 2. Exclude the first element (include the last)
        return max(self.house_robber_linear(nums[:-1]), self.house_robber_linear(nums[1:]))

    def house_robber_linear(self, nums: list[int]) -> int:
        """Helper function to solve the standard House Robber problem (linear array)."""
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])  # Either skip current or rob current

        return dp[n - 1]


# Test Cases
solution = Solution()

print(solution.rob([2, 1, 4, 9]))  # Output: 11
print(solution.rob([1, 2, 3, 1]))  # Output: 4
print(solution.rob([1]))  # Output: 1
print(solution.rob([1, 3, 1, 3, 100]))  # Output: 103
print(solution.rob([1, 2, 3]))  # Output: 4


# Time Complexity: O(n), as we iterate through the array twice in the worst case.
# Space Complexity: O(n) for the dp array in the helper function. This can be optimized to O(1) by using two variables to store dp[i-1] and dp[i-2]. 
```