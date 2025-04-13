```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular array of integers nums, return the maximum sum of a non-adjacent subset of elements.
# In a circular array, the first and last elements are considered adjacent.

# Examples:
# Example 1:
# Input: nums = [2, 7, 9, 3, 1]
# Output: 11
# Explanation: Choose elements at index 0, 2, and 4 (2 + 9 + 1 = 12) or choose elements at index 1 and 3 (7 + 3 = 10).
# Example given was incorrect.  Correct answer is 11.

# Example 2:
# Input: nums = [1, 2, 3, 1]
# Output: 4
# Explanation: Choose elements at index 0 and 2 (1 + 3 = 4).

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
        # 1. Include the first element: Then we cannot include the last element.
        # 2. Exclude the first element: Then we can include the last element.

        def house_robber(arr):  # Helper function for standard house robber problem (linear array)
            n = len(arr)
            dp = [0] * n
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])
            for i in range(2, n):
                dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])
            return dp[-1]

        # Scenario 1: Exclude last element
        max1 = house_robber(nums[:-1])
        
        # Scenario 2: Exclude first element
        max2 = house_robber(nums[1:])

        return max(max1, max2)

# Time Complexity: O(n), where n is the length of the input array, due to the linear traversal in the house_robber helper function.
# Space Complexity: O(n) for the dp array in the house_robber helper function. Could be optimized to O(1)


# Test cases
solution = Solution()

print(solution.rob([2, 7, 9, 3, 1]))  # Output: 11
print(solution.rob([1, 2, 3, 1]))  # Output: 4
print(solution.rob([1, 2, 3]))  # Output: 3 (either 1 + 3 = 4 or 2)
print(solution.rob([2,3,2])) # Output: 3
print(solution.rob([1,3,1,3,100])) # Output 103

```