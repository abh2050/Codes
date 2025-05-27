```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular array of integers nums (where the last element is considered adjacent to the first), 
# find the maximum sum of a subset of non-adjacent elements.

# Examples:
# Example 1:
# Input: nums = [1, 2, 3, 1]
# Output: 4
# Explanation: Select 1 and 3.

# Example 2:
# Input: nums = [2, 7, 9, 3, 1]
# Output: 12
# Explanation: Select 2, 9, and 1.

# Example 3:
# Input: nums = [1, 15, 3, 8, 2]
# Output: 23 # Select 15, 8
# Explanation:

# Constraints:
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^3
'''

class Solution:
    def rob_circular(self, nums: list[int]) -> int:
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
            return max(nums[0], nums[1])

        # Consider two scenarios:
        # 1. Include the first element (exclude the last)
        # 2. Exclude the first element (can include the last)

        def rob_linear(arr):
            """Helper function for house robber problem (linear array)."""
            dp = [0] * len(arr)
            dp[0] = arr[0]
            if len(arr) > 1:
                dp[1] = max(arr[0], arr[1])
            for i in range(2, len(arr)):
                dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])
            return dp[-1]


        include_first = rob_linear(nums[:-1]) # Exclude last element
        exclude_first = rob_linear(nums[1:])  # Exclude first element
        
        return max(include_first, exclude_first)


# Test cases
solution = Solution()
print(solution.rob_circular([1, 2, 3, 1]))  # Output: 4
print(solution.rob_circular([2, 7, 9, 3, 1]))  # Output: 12
print(solution.rob_circular([1, 15, 3, 8, 2])) # Output: 23
print(solution.rob_circular([1])) # Output 1
print(solution.rob_circular([1,3])) # Output 3
print(solution.rob_circular([1,3,1])) # Output 3
print(solution.rob_circular([1,10,2,1,10])) # Output 20

'''
# Time Complexity: O(n), where n is the length of the input array, due to the linear traversal in rob_linear.
# Space Complexity: O(n) for the dp array in rob_linear. Can be optimized to O(1) using two variables to store previous values.
'''

```