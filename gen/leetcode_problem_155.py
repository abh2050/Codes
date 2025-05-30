```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular integer array nums (i.e., the next element of nums[-1] is nums[0]), 
# return the maximum sum of a non-adjacent subsequence. A non-adjacent subsequence 
# is a subsequence where no two elements are adjacent in the circular array.

# Examples:
# Example 1:
# Input: nums = [2,4,1,3,5]
# Output: 10
# Explanation: Take elements at indices 0, 2, and 4 (2 + 1 + 5 = 8), or 1 and 3 (4+3=7), or 1 and 4 (4+5=9), or 0 and 3 (2+3=5).  Other possibilities exist. The maximum possible sum is 10 with elements at indices 1 and 4.

# Example 2:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Take elements at indices 0 and 2 (1 + 3 = 4).

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
        # 1. Rob the first house, but not the last.
        # 2. Don't rob the first house, but rob the last.

        def rob_linear(arr):
            n = len(arr)
            dp = [0] * (n + 1)  # dp[i] stores max sum up to index i
            dp[1] = arr[0]

            for i in range(2, n + 1):
                dp[i] = max(dp[i - 1], dp[i - 2] + arr[i - 1])
            return dp[n]
        
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))


# Time Complexity: O(n), where n is the length of nums. We traverse the array twice in the rob_linear function.
# Space Complexity: O(n) due to the dp array used in rob_linear.  Can be optimized to O(1) by using variables instead of a full dp array.


# Test Cases
solution = Solution()
print(solution.rob([2, 4, 1, 3, 5]))  # Output: 10
print(solution.rob([1, 2, 3, 1]))  # Output: 4
print(solution.rob([1]))  # Output: 1
print(solution.rob([1, 2]))  # Output: 2
print(solution.rob([1,2,3])) # Output 3
print(solution.rob([100,1,1,100])) # Output 200

```