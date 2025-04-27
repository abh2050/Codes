```python
'''
# Check if Number is Within Range
# Difficulty: Easy

# Problem Description:
# Given an integer `num` and two integers `lower` and `upper`, return `True` if `num` is within the inclusive range [lower, upper], otherwise return `False`.

# Examples:
# Example 1:
# Input: num = 5, lower = 1, upper = 10
# Output: True
# Explanation: 5 is within the range [1, 10].

# Example 2:
# Input: num = 15, lower = 1, upper = 10
# Output: False
# Explanation: 15 is outside the range [1, 10].

# Example 3:
# Input: num = 1, lower = 1, upper = 1
# Output: True
# Explanation: 1 is within the range [1, 1].


# Constraints:
# -100 <= num <= 100
# -100 <= lower <= 100
# -100 <= upper <= 100
'''

class Solution:
    def isWithinRange(self, num: int, lower: int, upper: int) -> bool:
        """
        Checks if a number is within the inclusive range [lower, upper].

        Args:
            num: The integer to check.
            lower: The lower bound of the range (inclusive).
            upper: The upper bound of the range (inclusive).

        Returns:
            True if num is within the range [lower, upper], False otherwise.
        """
        # Simply check if num is greater than or equal to lower and less than or equal to upper.
        return lower <= num <= upper


# Time Complexity: O(1) - Constant time, as we perform a simple comparison.
# Space Complexity: O(1) - Constant space, as we don't use any extra space.



# Test Cases
solution = Solution()

print(solution.isWithinRange(5, 1, 10))  # Output: True
print(solution.isWithinRange(15, 1, 10)) # Output: False
print(solution.isWithinRange(1, 1, 1))  # Output: True
print(solution.isWithinRange(-5, -10, 0))  # Output: True
print(solution.isWithinRange(100, 0, 99))  # Output: False

```