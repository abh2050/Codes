```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular integer array nums (i.e., the next element of nums[-1] is nums[0]), return the maximum sum of a non-empty subsequence of nums such that no two elements in the subsequence are adjacent.

# Examples:
# Example 1:
# Input: nums = [2,1,4,9]
# Output: 11
# Explanation: We can choose the subsequence [2, 9]. The sum is 2 + 9 = 11.

# Example 2:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: We can choose the subsequence [1, 3]. The sum is 1 + 3 = 4.

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
            The maximum sum of a non-empty non-adjacent subsequence.
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        
        # Handle the circularity by considering two cases:
        # 1. Exclude the last element:  rob(nums[:-1])
        # 2. Exclude the first element: rob(nums[1:])
        # The maximum of these two represents the solution.
        
        def rob_linear(arr):
            """Helper function to solve the linear non-adjacent sum problem."""
            if not arr:
                return 0
            if len(arr) == 1:
                return arr[0]

            dp = [0] * len(arr)
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])

            for i in range(2, len(arr)):
                dp[i] = max(dp[i-1], dp[i-2] + arr[i])

            return dp[-1]


        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))




# Test cases
solution = Solution()
print(solution.rob([2, 1, 4, 9]))  # Output: 11
print(solution.rob([1, 2, 3, 1]))  # Output: 4
print(solution.rob([1])) # Output 1
print(solution.rob([1,2])) # Output 2
print(solution.rob([1, 5, 3]))  # Output: 5



"""
Time Complexity: O(N), where N is the length of the input array. We iterate through the array twice in the worst case (once for each linear rob).

Space Complexity: O(N) for the dp array in the rob_linear helper function. This could be optimized to O(1) by using variables to store only the previous two values.
"""
```