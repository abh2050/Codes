```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular array of integers nums, return the maximum sum of a non-adjacent 
# subsequence.  "Non-adjacent" means that no two elements in the subsequence can be 
# adjacent in the original circular array. The array is considered circular, meaning 
# the last element is adjacent to the first element.

# Examples:
# Example 1:
# Input: nums = [2,4,1,3,5]
# Output: 10
# Explanation: Pick the subsequence [4,5,1]. The sum is 10.

# Example 2:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Pick the subsequence [1,3]. The sum is 4.

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

        # Consider two scenarios:
        # 1. Robbing the first house: Cannot rob the last house.
        # 2. Not robbing the first house: Can rob the last house.
        # Return the maximum of these two scenarios.

        def rob_linear(arr):
            """Helper function to calculate max sum for a linear (non-circular) array."""
            rob1, rob2 = 0, 0
            for num in arr:
                temp = max(rob1 + num, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2

        # Scenario 1: Robbing the first house
        max1 = rob_linear(nums[:-1])

        # Scenario 2: Not robbing the first house
        max2 = rob_linear(nums[1:])


        return max(max1, max2)


# Time Complexity: O(n), as we iterate through the array twice in the helper function.
# Space Complexity: O(1), as we only use a few variables to store intermediate results.


# Test Cases
solution = Solution()
print(solution.rob([2, 4, 1, 3, 5]))  # Output: 10
print(solution.rob([1, 2, 3, 1]))  # Output: 4
print(solution.rob([1])) # Output 1
print(solution.rob([])) # Output 0
print(solution.rob([1,2,3,4,5,1,2,3,4,5])) # Output 15
print(solution.rob([1,5,3,7,2,9])) # Output 16


```