```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular integer array nums, return the maximum possible sum of a non-empty subarray of nums, where non-adjacent elements are picked.
# A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n], where n is the length of nums.
# A subarray may only include each element of the original array once.

# Examples:
# Example 1:
# Input: nums = [2,7,9,3,1]
# Output: 11
# Explanation: Pick nums[0] = 2, nums[2] = 9, and nums[4] = 1. The sum is 2 + 9 + 1 = 11.

# Example 2:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Pick nums[0] = 1 and nums[2] = 3. The sum is 1 + 3 = 4.

# Constraints:
# 1 <= nums.length <= 5 * 10^4
# -10^4 <= nums[i] <= 10^4
'''

class Solution:
    def rob(self, nums: list[int]) -> int:
        """
        Calculates the maximum sum of non-adjacent elements in a circular array.

        Args:
            nums: The input circular integer array.

        Returns:
            The maximum possible sum.
        """
        n = len(nums)
        if n == 1:
            return nums[0]

        # Consider two cases:
        # 1. Robbing the first house (excluding the last)
        # 2. Not robbing the first house (including the last)
        return max(self.house_robber(nums[:-1]), self.house_robber(nums[1:]))
    

    def house_robber(self, nums: list[int]) -> int:
        """Helper function to solve the standard house robber problem (linear array)."""
        n = len(nums)
        if not nums:
            return 0
        if n == 1:
            return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp[n-1]

# Time Complexity: O(N) - We iterate through the array twice in the worst case.
# Space Complexity: O(N) -  Due to the dp array in the house_robber function.  Could be optimized to O(1)

# Test Cases
sol = Solution()

print(sol.rob([2, 7, 9, 3, 1]))  # Output: 11
print(sol.rob([1, 2, 3, 1]))  # Output: 4
print(sol.rob([1]))  # Output: 1
print(sol.rob([1, 2])) # Output 2
print(sol.rob([1,3,1,3,100])) # Output 103

```