```python
'''
# Check if Number is Within Range
# Difficulty: Easy

# Problem Description:
# Given an integer `num` and a closed interval defined by integers `lower` and `upper` (inclusive), 
# return `True` if `num` falls within the interval, and `False` otherwise.

# Examples:
# Example 1:
# Input: num = 5, lower = 1, upper = 10
# Output: True
# Explanation: 5 is within the interval [1, 10].

# Example 2:
# Input: num = 15, lower = 1, upper = 10
# Output: False
# Explanation: 15 is outside the interval [1, 10].

# Example 3:
# Input: num = 1, lower = 1, upper = 1
# Output: True
# Explanation: 1 is within the interval [1, 1].


# Constraints:
# -100 <= num <= 100
# -100 <= lower <= 100
# -100 <= upper <= 100
# lower <= upper 
'''

class Solution:
    def isWithinRange(self, num: int, lower: int, upper: int) -> bool:
        """
        Checks if a number is within a given range (inclusive).

        Args:
            num: The integer to check.
            lower: The lower bound of the interval.
            upper: The upper bound of the interval.

        Returns:
            True if num is within the interval [lower, upper], False otherwise.
        """
        # Check if num is greater than or equal to lower and less than or equal to upper.
        return lower <= num <= upper


# Time Complexity: O(1) - Constant time, as we perform a simple comparison.
# Space Complexity: O(1) - Constant space, as we don't use any extra space.



# Test cases
solution = Solution()

print(solution.isWithinRange(5, 1, 10))  # Output: True
print(solution.isWithinRange(15, 1, 10)) # Output: False
print(solution.isWithinRange(1, 1, 1))  # Output: True
print(solution.isWithinRange(-5, -10, 0)) # Output: True
print(solution.isWithinRange(100, 0, 99)) # Output: False

```