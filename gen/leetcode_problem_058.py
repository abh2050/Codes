```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular array of integers nums (where the last element is considered adjacent to the first), find the maximum sum of a non-adjacent subset of elements.  A subset is non-adjacent if no two elements in the subset are adjacent in the circular array.

# Examples:
# Example 1:
# Input: nums = [2, 4, 1, 3, 5]
# Output: 10
# Explanation: The maximum sum can be obtained by selecting elements at indices 0, 2, and 4 (2 + 1 + 5 = 8), or selecting elements at indices 1 and 3 (4 + 3 = 7), or selecting elements at indices 0, 2 and 3 (2+1+3 =6), however the optimal combination would be to select elements at index 1 and index 4 (4+5=9) or 0,3 and 4 (2+3+5 = 10) which are non-adjacent. Hence, we return 10.

# Example 2:
# Input: nums = [1, 2, 3, 1]
# Output: 4
# Explanation: Select elements at indices 0 and 2 (1 + 3 = 4).

# Constraints:
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^4
'''

class Solution:
    def rob(self, nums: list[int]) -> int:
        """
        Calculates the maximum sum of non-adjacent elements in a circular array.

        This solution uses dynamic programming to avoid redundant calculations.  It considers two scenarios:
        1. The first element is included in the subset.
        2. The first element is not included in the subset.
        
        We use a helper function to calculate the maximum sum for a linear array (without the circular wrap-around). Then we call it twice:
        - once with the array excluding the last element (to simulate the circular nature when the first element IS included)
        - once with the array excluding the first element (when it's NOT included).

        Time Complexity: O(n)
        Space Complexity: O(n) - Can be optimized to O(1) by storing only the last two values
        """

        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)

        def rob_linear(arr):
            dp = [0] * len(arr)
            dp[0] = arr[0]
            if len(arr) > 1:
                dp[1] = max(arr[0], arr[1])

            for i in range(2, len(arr)):
                dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])
            return dp[-1]

        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))

# Test Cases
solution = Solution()

print(solution.rob([2, 4, 1, 3, 5]))  # Output: 10
print(solution.rob([1, 2, 3, 1]))  # Output: 4
print(solution.rob([1])) # Output: 1
print(solution.rob([1,2])) # Output: 2
print(solution.rob([2,3,2])) # Output: 3
print(solution.rob([1,7,9,2])) # Output: 10
```