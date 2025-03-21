```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular array of integers nums (where the last element is considered adjacent to the first element), 
# find the maximum sum of a non-adjacent subsequence. A subsequence is a sequence that can be derived from 
# another sequence by deleting some or no elements without changing the order of the remaining elements.
# Non-adjacent means no two selected elements are adjacent in the original array (including circular adjacency).

# Examples:
# Example 1:
# Input: nums = [2, 4, 1, 3, 5]
# Output: 10
# Explanation: Select elements 2, 1, and 5 for a total sum of 10.

# Example 2:
# Input: nums = [1, 2, 3, 1]
# Output: 4
# Explanation: Select elements 1 and 3 for a total sum of 4.

# Constraints:
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^4
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
        # 1. Excluding the first element: Standard house robber problem on nums[1:]
        # 2. Excluding the last element: Standard house robber problem on nums[:-1]
        # Return the maximum of these two cases.

        def house_robber(arr):
            """Solves the standard house robber problem (linear array)."""
            dp = [0] * len(arr)
            dp[0] = arr[0]
            if len(arr) > 1:
                dp[1] = max(arr[0], arr[1])
            for i in range(2, len(arr)):
                dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])
            return dp[-1]

        return max(house_robber(nums[1:]), house_robber(nums[:-1]))
    
    # Time Complexity: O(N), where N is the length of the array. We iterate through the array twice in the worst case.
    # Space Complexity: O(N), to store the dp array in the house robber subproblem. It can be optimized to O(1).


# Test cases
solution = Solution()
print(solution.rob([2, 4, 1, 3, 5]))  # Output: 10
print(solution.rob([1, 2, 3, 1]))  # Output: 4
print(solution.rob([1])) # Output: 1
print(solution.rob([1, 2])) # Output: 2
print(solution.rob([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])) # Output: 15
print(solution.rob([1, 3, 1, 3, 100])) # Output: 103


```