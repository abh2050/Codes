```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular array of integers nums, return the maximum sum of a non-adjacent subsequence. 
# In a circular array, the last element is considered adjacent to the first element. 
# A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

# Examples:
# Example 1:
# Input: nums = [2,4,6,2]
# Output: 10
# Explanation: You can choose subsequence [4,6] or [2,6] for a total sum of 10.

# Example 2:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: You can choose the subsequence [1,3] for a total sum of 4.

# Example 3:
# Input: nums = [1]
# Output: 1

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
            The maximum sum of a non-adjacent subsequence.
        """
        n = len(nums)
        if n == 1:
            return nums[0]

        # We consider two scenarios:
        # 1. Robbing the first house, so we can't rob the last house.
        # 2. Not robbing the first house, so we can rob the last house.
        # We take the maximum of these two scenarios.
        return max(self.house_robber_1(nums[:-1]), self.house_robber_1(nums[1:]))


    def house_robber_1(self, nums: list[int]) -> int:
        """Helper function to calculate max sum of non-adjacent elements in a linear array (House Robber I problem)."""
        n = len(nums)
        if n == 0:  # Handle empty array for edge cases when nums has length 1 or 2
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
print(solution.rob([2, 4, 6, 2]))  # Output: 10
print(solution.rob([1, 2, 3, 1]))  # Output: 4
print(solution.rob([1]))  # Output: 1
print(solution.rob([1,2])) # Output: 2
print(solution.rob([2,7,9,3,1])) # Output: 11
print(solution.rob([1,3,1,3,100])) # Output: 103




```

**Explanation:**

1. **Circular Array Handling:** The key idea is to reduce the circular array problem to the linear array House Robber problem.  Since the last element is adjacent to the first, we consider two scenarios: including the first element and excluding it.  By solving the linear House Robber problem for both scenarios, we effectively cover all possible non-adjacent subsequences in the circular array.

2. **`house_robber_1()` (Helper Function):** This function efficiently solves the standard House Robber problem (linear array) using dynamic programming.  `dp[i]` stores the maximum rob-able amount up to house `i`. The recurrence relation is `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`, meaning we either skip the current house or rob it (and therefore skip the previous house).

**Time and Space Complexity:**

- **Time Complexity:** O(n), where n is the length of the input array. We iterate through the array twice in the worst case (once for each scenario).
- **Space Complexity:** O(n) for the `dp` array in `house_robber_1()`.  This can be optimized to O(1) by using only two variables to store `dp[i-1]` and `dp[i-2]`, but for clarity, the O(n) solution is presented.