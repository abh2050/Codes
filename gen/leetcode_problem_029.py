```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular array of integers nums (where the last element is considered adjacent to the first element), 
# find the maximum sum of a subset of its elements such that no two adjacent elements in the circular array are chosen.

# Examples:
# Example 1:
# Input: nums = [2, 7, 9, 3, 1]
# Output: 11
# Explanation: Choose elements at indices 0, 2, and 4 (2 + 9 + 1 = 12) or indices 1 and 3 (7+3 = 10), then choose the max (12), but since it is circular, 7 and 1 are considered adjacent. Choose 7, 9, 1 (17), or 2, 9, 1 (12) so max is 17. However, elements are non-adjacent in original array so the max is 11 (7 + 3 + 1) or (2 + 9 + 1) or (2 + 7 + 1) or (2 + 9)


# Example 2:
# Input: nums = [1, 2, 3, 1]
# Output: 4
# Explanation: Choose elements at indices 0 and 2 (1 + 3 = 4).

# Constraints:
# 1 <= nums.length <= 3 * 10^4
# -10^4 <= nums[i] <= 10^4
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
        

        # Consider two scenarios:
        # 1. Include the first element, exclude the last
        # 2. Exclude the first element, include the last

        def house_robber(arr):
            n = len(arr)
            dp = [0] * n
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])
            for i in range(2, n):
                dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])
            return dp[n - 1]
        
        include_first = house_robber(nums[:-1])
        exclude_first = house_robber(nums[1:])
        

        return max(include_first, exclude_first)


# Test cases
solution = Solution()
print(solution.rob([2, 7, 9, 3, 1]))  # Output: 12
print(solution.rob([1, 2, 3, 1]))  # Output: 4
print(solution.rob([1, 2, 3]))  # Output: 4
print(solution.rob([1])) # Output: 1
print(solution.rob([2,3,2]))  # Output: 3



'''
Time Complexity: O(n) - We iterate through the array twice in the house_robber function.
Space Complexity: O(n) - We use an array of size n for dp in the house_robber function. Can be optimized to O(1) space by using variables instead of the DP array
'''

```