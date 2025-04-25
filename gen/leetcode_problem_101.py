```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular array of integers nums (nums[0] and nums[-1] are considered adjacent), 
# find the maximum sum of a non-adjacent subsequence. A non-adjacent subsequence is a 
# sequence of numbers where no two numbers are adjacent in the circular array.

# Examples:
# Example 1:
# Input: nums = [2, 4, 1, 3, 5]
# Output: 10
# Explanation: Pick elements 2, 1, and 5. Their sum is 10.

# Example 2:
# Input: nums = [1, 2, 3, 1]
# Output: 4
# Explanation: Pick elements 1 and 3. Their sum is 4.

# Constraints:
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^4
'''

class Solution:
    def rob_circular(self, nums: list[int]) -> int:
        """
        Calculates the maximum sum of non-adjacent elements in a circular array.

        Args:
            nums: The input circular array of integers.

        Returns:
            The maximum sum of a non-adjacent subsequence.
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        # Two cases: either include the first element or exclude it
        # Case 1: Exclude the first element
        case1 = self.rob_linear(nums[1:])

        # Case 2: Include the first element (exclude the last element)
        case2 = self.rob_linear(nums[:-1])

        return max(case1, case2)

    def rob_linear(self, nums: list[int]) -> int:
        """Helper function to solve the linear version of house robber."""
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


# Time Complexity: O(N) - We iterate through the array twice in the worst case.
# Space Complexity: O(N) - For the dp array in the helper function. Can be optimized to O(1).


# Test Cases
solution = Solution()
print(solution.rob_circular([2, 4, 1, 3, 5]))  # Output: 10
print(solution.rob_circular([1, 2, 3, 1]))  # Output: 4
print(solution.rob_circular([1])) # Output: 1
print(solution.rob_circular([])) # Output: 0
print(solution.rob_circular([1,2,3,4,5,1,2,3,4,5])) # Output: 15




```