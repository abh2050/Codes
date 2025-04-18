```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular integer array nums (i.e., the next element of nums[-1] is nums[0]), 
# return the maximum sum of a non-adjacent subset of nums.
# A non-adjacent subset is a subset where no two elements are adjacent in the circular array.

# Examples:
# Example 1:
# Input: nums = [2,7,9,3,1]
# Output: 11
# Explanation: Choose nums[0] = 2, nums[2] = 9, and nums[4] = 1. The sum is 12.
# Note that nums[0] and nums[4] are not adjacent as the array is circular.


# Example 2:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Choose nums[0] = 1 and nums[2] = 3. The sum is 4.

# Constraints:
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
'''

class Solution:
    def rob(self, nums: list[int]) -> int:
        """
        Calculates the maximum sum of non-adjacent elements in a circular array.

        Args:
            nums: The input circular integer array.

        Returns:
            The maximum sum of a non-adjacent subset.
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)

        # Consider two cases:
        # 1. Rob the first house, don't rob the last house.
        # 2. Don't rob the first house, possibly rob the last house.
        return max(self.house_robber_linear(nums[:-1]), self.house_robber_linear(nums[1:]))


    def house_robber_linear(self, nums: list[int]) -> int:
        """
        Helper function to solve the standard house robber problem (linear array).
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
solution = Solution()

print(solution.rob([2, 7, 9, 3, 1]))  # Output: 11
print(solution.rob([1, 2, 3, 1]))  # Output: 4
print(solution.rob([1,2,3])) # Output 4
print(solution.rob([2,3,2])) # Output 3
print(solution.rob([1,3,1,3,100])) # Output: 103




# Time Complexity: O(n), where n is the length of nums. We iterate through the array twice in the worst case using the house_robber_linear helper function.
# Space Complexity: O(n) for the dp array in house_robber_linear. Could be optimized to O(1) by using variables to track the previous two maximums.


```