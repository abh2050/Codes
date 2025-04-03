```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular array of integers nums (where the last element is considered adjacent to the first element), 
# find the maximum sum of a subset of non-adjacent elements.

# Examples:
# Example 1:
# Input: nums = [2, 7, 9, 3, 1]
# Output: 11
# Explanation: Select elements at indices 0, 2, and 4 (2 + 9 + 1 = 12). Alternatively, you can select 7 + 3 = 10 or 7+1=8 or 9+1=10. 11 is the maximum possible sum of non-adjacent elements.

# Example 2:
# Input: nums = [1, 2, 3, 1]
# Output: 4
# Explanation: Select elements at indices 0 and 2 (1 + 3 = 4).

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
            The maximum sum of non-adjacent elements.
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)

        # Consider two cases:
        # 1. Include the first element: Then we can't include the last element.
        # 2. Exclude the first element: Then we can include the last element.

        # Case 1: Exclude last element
        dp1 = [0] * (n - 1)
        dp1[0] = nums[0]
        dp1[1] = max(nums[0], nums[1])
        for i in range(2, n - 1):
            dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i])

        # Case 2: Exclude first element
        dp2 = [0] * n
        dp2[1] = nums[1]
        for i in range(2, n):
            dp2[i] = max(dp2[i - 1], dp2[i - 2] + nums[i])

        return max(dp1[n - 2], dp2[n - 1])


# Time Complexity: O(n) - We iterate through the array twice in the two DP calculations.
# Space Complexity: O(n) - We use two DP arrays of size n.


# Test cases
sol = Solution()
print(sol.rob_circular([2, 7, 9, 3, 1]))  # Output: 12
print(sol.rob_circular([1, 2, 3, 1]))  # Output: 4
print(sol.rob_circular([1, 2, 3]))  # Output: 3
print(sol.rob_circular([1]))       # Output: 1
print(sol.rob_circular([1, 5]))     # Output: 5
print(sol.rob_circular([2,1,1,2])) # Output: 3


```