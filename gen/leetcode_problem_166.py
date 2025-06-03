```python
'''
# Alternating Sum
# Difficulty: Easy

# Problem Description:
# Given a non-empty list of integers nums, return the alternating sum.
# The alternating sum is calculated by subtracting the second element from the first, 
# adding the third element, subtracting the fourth, and so on.

# Examples:
# Example 1:
# Input: nums = [1, 2, 3, 4, 5]
# Output: 3
# Explanation: 1 - 2 + 3 - 4 + 5 = 3

# Example 2:
# Input: nums = [10, 5]
# Output: 5
# Explanation: 10 - 5 = 5

# Constraints:
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 1000
'''

class Solution:
    def alternatingSum(self, nums: list[int]) -> int:
        """
        Calculates the alternating sum of a list of integers.

        Args:
            nums: A list of integers.

        Returns:
            The alternating sum.
        """
        alt_sum = 0
        sign = 1  # Start with addition
        for num in nums:
            alt_sum += sign * num
            sign *= -1  # Alternate between addition and subtraction
        return alt_sum

# Time Complexity: O(n), where n is the length of the input list. We iterate through the list once.
# Space Complexity: O(1), we only use a few extra variables for the sum and sign, regardless of the input size.



# Test Cases
solution = Solution()

print(solution.alternatingSum([1, 2, 3, 4, 5]))  # Output: 3
print(solution.alternatingSum([10, 5]))  # Output: 5
print(solution.alternatingSum([1]))  # Output: 1
print(solution.alternatingSum([1, 2, 3, 4, 5, 6])) # Output: -3
print(solution.alternatingSum([100, 50, 25, 10])) # Output: 65


```