```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular integer array nums (i.e., the next element of nums[-1] is nums[0]), return the maximum sum of a non-empty subsequence of nums such that no two elements in the subsequence are adjacent in the circular array.

# Examples:
# Example 1:
# Input: nums = [2,1,3,1,5]
# Output: 9
# Explanation: Pick the subsequence [2, 3, 5]. 2, 3, and 5 are not adjacent in the circular array and their sum is 9.

# Example 2:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Pick the subsequence [2, 1]. Their sum is 4.

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
            The maximum sum of the non-adjacent subsequence.
        """
        n = len(nums)
        if n == 1:
            return nums[0]

        # We consider two scenarios:
        # 1. Excluding the last element (like House Robber I)
        # 2. Excluding the first element (like House Robber I)
        # The maximum of these two scenarios gives the answer for the circular array.

        def house_robber(arr):
            dp = [0] * len(arr)
            dp[0] = arr[0]
            if len(arr) > 1:
                dp[1] = max(arr[0], arr[1])
            for i in range(2, len(arr)):
                dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])
            return dp[-1]

        return max(house_robber(nums[:-1]), house_robber(nums[1:]))


# Time Complexity: O(n) - We iterate through the array twice in the house_robber function.
# Space Complexity: O(n) -  We use a dp array of size n in the house_robber function. Could be optimized to O(1) using variables instead of the dp array.



# Test cases
solution = Solution()
print(solution.rob([2, 1, 3, 1, 5]))  # Output: 9
print(solution.rob([1, 2, 3, 1]))  # Output: 4
print(solution.rob([1]))  # Output: 1
print(solution.rob([1, 2])) # Output: 2
print(solution.rob([1, 2, 3])) # Output 4
print(solution.rob([100,1,1,100])) # Output: 200

```