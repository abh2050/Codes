```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular array of integers nums (where the last element is considered adjacent to the first element), 
# find the maximum sum of a non-adjacent subset of elements.  A subset is non-adjacent if no two elements in the subset are directly next to each other in the array (including wrapping around).

# Examples:
# Example 1:
# Input: nums = [2, 4, 1, 3, 5]
# Output: 10
# Explanation: The maximum sum can be obtained by selecting [2, 1, 5].

# Example 2:
# Input: nums = [1, 2, 3, 1]
# Output: 4
# Explanation: The maximum sum can be obtained by selecting [1, 3].

# Constraints:
# 1 <= nums.length <= 10^5
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

        # Consider two cases:
        # 1. Include the first element (exclude the last)
        # 2. Exclude the first element (can include the last)
        return max(self.rob_linear(nums[:-1]), self.rob_linear(nums[1:]))

    def rob_linear(self, nums: list[int]) -> int:
        """
        Helper function to calculate the maximum sum of non-adjacent elements in a linear array (House Robber I).
        Uses dynamic programming.

        Args:
            nums: The linear array.

        Returns:
            Maximum sum of a non-adjacent subset.
        """
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i]) # either skip current, or take current and previous best excluding adjacent

        return dp[n-1]


# Test Cases
solution = Solution()

print(solution.rob_circular([2, 4, 1, 3, 5]))  # Output: 10
print(solution.rob_circular([1, 2, 3, 1]))  # Output: 4
print(solution.rob_circular([1]))  # Output: 1
print(solution.rob_circular([])) # Output: 0
print(solution.rob_circular([1,7,9,2])) # Output: 10

# Time Complexity: O(N), where N is the length of the nums array. We iterate through the array twice in the worst case (once for each linear rob).
# Space Complexity: O(N) for the dp array in the linear rob function.  Could be optimized to O(1) by using variables to store previous states instead of the whole dp array.
```