```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular integer array nums (i.e., the first element is considered adjacent to the last element),
# find the maximum sum of a non-adjacent subset of elements.  A non-adjacent subset means no two elements
# in the subset are adjacent in the circular array.

# Examples:
# Example 1:
# Input: nums = [2, 7, 9, 3, 1]
# Output: 11
# Explanation: Pick numbers 2, 9, and 1.

# Example 2:
# Input: nums = [1, 2, 3, 1]
# Output: 4
# Explanation: Pick numbers 1 and 3.

# Constraints:
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
'''

class Solution:
    def rob_circular(self, nums: list[int]) -> int:
        """
        Calculates the maximum sum of non-adjacent elements in a circular array.

        Args:
            nums: The circular integer array.

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

        # Consider two scenarios:
        # 1. Include the first element (exclude the last)
        # 2. Exclude the first element (can include the last)
        return max(self.rob_linear(nums[:-1]), self.rob_linear(nums[1:]))


    def rob_linear(self, nums: list[int]) -> int:
        """Helper function to solve the linear non-adjacent sum problem (House Robber)."""
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


# Test Cases
solution = Solution()

print(solution.rob_circular([2, 7, 9, 3, 1]))  # Output: 11
print(solution.rob_circular([1, 2, 3, 1]))  # Output: 4
print(solution.rob_circular([1]))  # Output: 1
print(solution.rob_circular([1, 2])) # Output: 2
print(solution.rob_circular([1, 2, 3])) # Output: 3
print(solution.rob_circular([1, 5, 3, 2, 6])) # Output: 12



'''
Time Complexity: O(N) - We iterate through the array twice in the worst case (rob_linear is called twice).
Space Complexity: O(N) -  The dp array in rob_linear uses linear space.  Could be optimized to O(1) space by using variables instead of the dp array.
'''

```