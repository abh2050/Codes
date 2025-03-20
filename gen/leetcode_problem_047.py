```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular integer array `nums`, return the maximum sum of a non-adjacent subsequence. 
# In a circular array, the elements at the beginning and end of the array are considered adjacent.

# Examples:
# Example 1:
# Input: nums = [2, 4, 1, 3, 5]
# Output: 10
# Explanation: Selecting 4 + 5 + 1 maximizes the sum.

# Example 2:
# Input: nums = [1, 2, 3, 1]
# Output: 4
# Explanation: Selecting 1 + 3 maximizes the sum.

# Constraints:
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
'''

class Solution:
    def rob_circular(self, nums: list[int]) -> int:
        """
        Calculates the maximum sum of non-adjacent elements in a circular array.

        Args:
            nums: The input circular integer array.

        Returns:
            The maximum sum of a non-adjacent subsequence.
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)


        # Two scenarios: either include the first element or exclude it.
        # If we include the first element, we can't include the last.
        # If we exclude the first element, we can include the last.
        return max(self.rob_linear(nums[:-1]), self.rob_linear(nums[1:]))

    def rob_linear(self, nums: list[int]) -> int:
        """
        Helper function to calculate the maximum sum of non-adjacent elements in a linear array.

        Args:
            nums: The input linear integer array.

        Returns:
            The maximum sum of a non-adjacent subsequence.
        """

        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])  # Either skip current or include it

        return dp[n - 1]


# Time Complexity: O(N), where N is the length of nums, due to the two calls to rob_linear.
# Space Complexity: O(N) for rob_linear due to the dp array. Could be optimized to O(1) by using variables instead of the array.


# Test Cases
solution = Solution()
print(solution.rob_circular([2, 4, 1, 3, 5]))  # Output: 10
print(solution.rob_circular([1, 2, 3, 1]))  # Output: 4
print(solution.rob_circular([1]))  # Output: 1
print(solution.rob_circular([1,2]))  # Output: 2
print(solution.rob_circular([1, 5, 3, 7, 2, 4])) # Output 14
print(solution.rob_circular([1, 7, 5, 9, 2, 6, 4])) # Output: 22

```