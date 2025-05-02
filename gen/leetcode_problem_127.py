```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular array of integers nums (where the last element is considered adjacent to the first element), 
# find the maximum sum of a non-adjacent subset of elements. A non-adjacent subset means no two elements in the subset are adjacent in the array, including the first and last elements.

# Examples:
# Example 1:
# Input: nums = [2, 7, 9, 3, 1]
# Output: 11
# Explanation: The maximum sum can be achieved by selecting nums[0] (2), nums[2] (9), and nums[4] (1). The sum is 2 + 9 + 1 = 12

# Example 2:
# Input: nums = [1, 2, 3, 1]
# Output: 4
# Explanation: The maximum sum can be achieved by selecting nums[0] (1) and nums[2] (3). The sum is 1 + 3 = 4

# Example 3:
# Input: nums = [1]
# Output: 1

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
            The maximum sum of a non-adjacent subset.
        """
        n = len(nums)
        if n == 1:
            return nums[0]

        # Two scenarios: either we include the first element or we don't
        # 1. Exclude the last element (equivalent to the standard house robber problem)
        def houseRobber(arr):
            dp = [0] * len(arr)
            dp[0] = arr[0]
            if len(arr) > 1:
                dp[1] = max(arr[0], arr[1])
            for i in range(2, len(arr)):
                dp[i] = max(dp[i-1], dp[i-2] + arr[i])
            return dp[-1]

        # Calculate the maximum sum for both scenarios
        include_first = houseRobber(nums[:-1])  # Exclude the last element
        exclude_first = houseRobber(nums[1:])  # Exclude the first element

        return max(include_first, exclude_first)


# Test cases
solution = Solution()
print(solution.rob([2, 7, 9, 3, 1]))  # Output: 11
print(solution.rob([1, 2, 3, 1]))  # Output: 4
print(solution.rob([1]))  # Output: 1
print(solution.rob([1,2,3])) # Output: 4
print(solution.rob([2,3,2])) # Output: 3



'''
Time Complexity: O(n) - We iterate through the array twice in the houseRobber function.
Space Complexity: O(n) - We use an array of size n for dp in the houseRobber function. 
However, this could be optimized to O(1) space by only storing the previous two dp values.
'''
```