```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular array of integers nums (where the first element is considered adjacent to the last element), 
# find the maximum sum of a subset where no two elements are adjacent.

# Examples:
# Example 1:
# Input: nums = [2, 7, 9, 3, 1]
# Output: 11
# Explanation: Pick nums[0] (2), nums[2] (9), and nums[4] (1). The sum is 11.

# Example 2:
# Input: nums = [1, 2, 3, 1]
# Output: 4
# Explanation: Pick nums[0] (1) and nums[2] (3). The sum is 4.

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
            The maximum sum of non-adjacent elements.
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)

        # Use dynamic programming to find the maximum sum for two cases:
        # 1. Excluding the last element (treating it as a linear array)
        # 2. Excluding the first element (treating it as a linear array)

        def house_robber(arr):
            """Helper function to solve the house robber problem for a linear array."""
            dp = [0] * len(arr)
            dp[0] = arr[0]
            if len(arr) > 1:
                dp[1] = max(arr[0], arr[1])
            for i in range(2, len(arr)):
                dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])  # Either skip current or include it
            return dp[-1]
            
        # Case 1: Exclude the last element
        max1 = house_robber(nums[:-1])

        # Case 2: Exclude the first element
        max2 = house_robber(nums[1:])

        return max(max1, max2)


# Test cases
solution = Solution()
print(solution.rob([2, 7, 9, 3, 1]))  # Output: 11
print(solution.rob([1, 2, 3, 1]))  # Output: 4
print(solution.rob([1, 2, 3]))  # Output: 3
print(solution.rob([1])) # Output 1
print(solution.rob([1,5])) # Output 5
print(solution.rob([2,3,2])) # Output 3


# Time Complexity: O(n), as we iterate through the array twice in the house_robber function.
# Space Complexity: O(n) for the dp array in the house_robber function. Can be optimized to O(1) by using variables instead of array.
```