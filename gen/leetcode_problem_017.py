```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular integer array nums, return the maximum possible sum of a non-empty subarray of nums, where no two elements in the subarray are adjacent. 
# In a circular array, the last element is considered adjacent to the first element.

# Examples:
# Example 1:
# Input: nums = [2,7,9,3,1]
# Output: 11
# Explanation: Choose the elements at indices 0, 2, and 4 (2 + 9 + 1 = 12).  However, since it's circular, 
# elements at indices 0 and 4 are considered adjacent, so the max sum would be 7 + 3 = 10, or 2 + 9 = 11, or 7 + 1 = 8.  11 is the largest possible sum.

# Example 2:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Choose the elements at indices 0 and 2 (1 + 3 = 4).

# Constraints:
# 1 <= nums.length <= 3 * 10^4
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
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)

        # Consider two scenarios:
        # 1. Rob the first house, then exclude the last house.
        # 2. Don't rob the first house, then potentially include the last house.
        return max(self.house_robber_linear(nums[:-1]), self.house_robber_linear(nums[1:]))

    def house_robber_linear(self, nums: list[int]) -> int:
        """Helper function to solve the standard house robber problem (linear array)."""
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i]) 
        return dp[n-1]



# Test Cases
solution = Solution()
print(solution.rob([2,7,9,3,1]))  # Output: 11
print(solution.rob([1,2,3,1]))  # Output: 4
print(solution.rob([1])) # Output: 1
print(solution.rob([1, 5])) # Output: 5
print(solution.rob([1,3,1,3,100])) # Output: 103
print(solution.rob([-1, -5])) # Output: -1


'''
Time Complexity: O(n), where n is the length of the input array. We iterate through the array twice in the worst case (once for each scenario).
Space Complexity: O(n) for the dp array in the house_robber_linear helper function.  Could be optimized to O(1) by using variables to store the previous two values instead of an array.
'''

```