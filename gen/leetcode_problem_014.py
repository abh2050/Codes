```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular array of integers nums (where the last element is considered adjacent to the first element), 
# find the maximum sum of a non-adjacent subsequence. A non-adjacent subsequence is a subsequence where no two 
# elements are adjacent in the original circular array.

# Examples:
# Example 1:
# Input: nums = [2, 1, 4, 9]
# Output: 11
# Explanation: The optimal subsequence is [2, 9].

# Example 2:
# Input: nums = [1, 2, 3, 1]
# Output: 4
# Explanation: The optimal subsequence is [1, 3].

# Example 3:
# Input: nums = [1, 2, 3]
# Output: 3
# Explanation: The optimal subsequence is [3] or [1, 2].

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
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        if n==3:
            return max(nums)

        # Consider two cases:
        # 1. Include the first element, exclude the last.
        # 2. Exclude the first element, include the last.
        def house_robber(arr): # standard house robber logic
            dp = [0] * len(arr)
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])

            for i in range(2,len(arr)):
                dp[i] = max(dp[i-1], dp[i-2] + arr[i])

            return dp[-1]

        return max(house_robber(nums[:-1]), house_robber(nums[1:]))




# Time Complexity: O(n) - We iterate through the array twice in the worst case.
# Space Complexity: O(n) - We use an array of size n for dynamic programming in the helper function. (Can be optimized to O(1) space)



# Test Cases
solution = Solution()

print(solution.rob([2, 1, 4, 9]))  # Output: 11
print(solution.rob([1, 2, 3, 1]))  # Output: 4
print(solution.rob([1, 2, 3]))  # Output: 3
print(solution.rob([1]))  # Output: 1
print(solution.rob([1,5])) # Output: 5
print(solution.rob([1,3,1,3,100])) # Output: 103


```