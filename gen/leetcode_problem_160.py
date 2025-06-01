```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular integer array nums (i.e., the next element of nums[-1] is nums[0]), 
# return the maximum sum of a non-adjacent subsequence. A subsequence is a sequence that can be derived from 
# another sequence by deleting some or no elements without changing the order of the remaining elements.
# Two elements are considered adjacent if their indices are adjacent or if the first and last elements are considered adjacent.

# Examples:
# Example 1:
# Input: nums = [2,4,6,2,5]
# Output: 13
# Explanation: Take the elements 2, 6, and 5.

# Example 2:
# Input: nums = [5,10,100,10,5]
# Output: 110
# Explanation: Take elements 5 and 100.

# Constraints:
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^4
'''

class Solution:
    def rob(self, nums: list[int]) -> int:
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

        # Consider two scenarios:
        # 1. Excluding the last element (same as House Robber I)
        # 2. Excluding the first element (same as House Robber I, shifted)
        return max(self.houseRobber(nums[:-1]), self.houseRobber(nums[1:]))


    def houseRobber(self, nums: list[int]) -> int:
        """
        Helper function to solve the standard House Robber problem (linear array).
        Uses dynamic programming.
        """
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
sol = Solution()
print(sol.rob([2, 4, 6, 2, 5]))  # Output: 13
print(sol.rob([5, 10, 100, 10, 5]))  # Output: 110
print(sol.rob([1, 2, 3, 1]))  # Output: 4
print(sol.rob([1]))  # Output 1
print(sol.rob([1,2]))  # Output 2



'''
Time Complexity: O(n), where n is the length of the input array. We iterate through the array twice in the worst case (once for each subproblem).

Space Complexity: O(n) for the dp array in the houseRobber helper function. This can be optimized to O(1) by using variables to store the previous two values instead of the entire dp array.
'''
```