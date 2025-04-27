```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular array of integers nums, return the maximum sum of a non-empty subsequence 
# such that no two elements in the subsequence are adjacent in the circular array.
# "Adjacent" means next to each other (i.e., index i and i+1 are adjacent, and index n-1 and 0 are adjacent).

# Examples:
# Example 1:
# Input: nums = [2,1,2,7,3]
# Output: 10
# Explanation: Take nums[0], nums[2], and nums[3]. The sum is 2 + 2 + 7 = 11 which is the maximum.
# Or nums[1], nums[3]. The sum is 1 + 7 = 8.
# Or nums[0], nums[2], nums[4]. The sum is 2 + 2 + 3 = 7.
# etc, so the maximum sum is 11.

# Example 2:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Take nums[0] and nums[2].

# Constraints:
# 1 <= nums.length <= 3 * 10^4
# -3 * 10^4 <= nums[i] <= 3 * 10^4
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

        # Consider two cases:
        # 1. Robbing the first house, but not the last.
        # 2. Not robbing the first house, but possibly robbing the last.
        return max(self.house_robber_i(nums[:-1]), self.house_robber_i(nums[1:]))

    def house_robber_i(self, nums: list[int]) -> int:
        """
        Helper function to solve the standard House Robber problem (linear array).

        Uses dynamic programming to store the maximum rob amount up to each house.
        """

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

print(solution.rob([2, 1, 2, 7, 3]))  # Output: 11
print(solution.rob([1, 2, 3, 1]))  # Output: 4
print(solution.rob([1])) # Output: 1
print(solution.rob([1, 2])) # Output: 2
print(solution.rob([1,3,1,3,100]))  # Output: 103

# Time Complexity: O(n), where n is the length of the input array.  We iterate through the array twice in house_robber_i.
# Space Complexity: O(n) in house_robber_i due to the dp array. Could be optimized to O(1) by using variables instead of the dp array.

```