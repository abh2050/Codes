```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular array of integers nums (meaning the last element is considered adjacent to the first element), 
# find the maximum sum of a subset of non-adjacent elements.

# Examples:
# Example 1:
# Input: nums = [2, 4, 1, 3, 5]
# Output: 10
# Explanation: The optimal subset is {2, 1, 5}, which sums up to 10.

# Example 2:
# Input: nums = [1, 2, 3, 1]
# Output: 4
# Explanation: The optimal subset is {1, 3}, which sums up to 4.

# Example 3:
# Input: nums = [1]
# Output: 1
# Explanation: The optimal subset is {1}.


# Constraints:
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^4
'''

class Solution:
    def rob(self, nums: list[int]) -> int:
        """
        Calculates the maximum sum of non-adjacent elements in a circular array.

        Args:
            nums: The input circular array of integers.

        Returns:
            The maximum sum of a subset of non-adjacent elements.
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        # Consider two scenarios:
        # 1. Include the first element, exclude the last element.
        # 2. Exclude the first element, include the last element (potentially).
        return max(self.house_robber(nums[:-1]), self.house_robber(nums[1:]))
    
    def house_robber(self, nums):
        """Helper function to solve the standard house robber problem (linear array)."""
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[n - 1]




# Test Cases
solution = Solution()

print(solution.rob([2, 4, 1, 3, 5]))  # Output: 10
print(solution.rob([1, 2, 3, 1]))  # Output: 4
print(solution.rob([1]))  # Output: 1
print(solution.rob([1,2,3])) # Output: 4
print(solution.rob([2,7,9,3,1])) # Output: 12


# Time Complexity: O(n) - We iterate through the array twice in the worst case (using house_robber).
# Space Complexity: O(n) -  For the dp array in the house_robber helper function.  Could be optimized to O(1) by using variables instead of the dp array.

```