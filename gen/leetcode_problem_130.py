```python
'''
# Sum of Even Digits
# Difficulty: Easy

# Problem Description:
# Given a non-negative integer num, return the sum of all its even digits.

# Examples:
# Example 1:
# Input: num = 2468
# Output: 20
# Explanation: The even digits are 2, 4, 6, and 8. Their sum is 2 + 4 + 6 + 8 = 20.

# Example 2:
# Input: num = 1357
# Output: 0
# Explanation: There are no even digits in the number.

# Example 3:
# Input: num = 12345
# Output: 6
# Explanation: The even digits are 2 and 4. Their sum is 2 + 4 = 6.


# Constraints:
# 0 <= num <= 10^9
'''

class Solution:
    def sumEvenDigits(self, num: int) -> int:
        """
        Calculates the sum of even digits in a given integer.

        Args:
            num: The non-negative integer.

        Returns:
            The sum of even digits.
        """

        sum_of_evens = 0
        for digit in str(num):  # Convert to string to iterate through digits
            digit = int(digit)  # Convert back to integer for arithmetic
            if digit % 2 == 0:
                sum_of_evens += digit
        return sum_of_evens

        # Time Complexity: O(log n) -  The number of digits in num is proportional to log10(num).
        # Space Complexity: O(1) - Constant extra space is used.


# Test cases
solution = Solution()
print(solution.sumEvenDigits(2468))  # Output: 20
print(solution.sumEvenDigits(1357))  # Output: 0
print(solution.sumEvenDigits(12345))  # Output: 6
print(solution.sumEvenDigits(0))    # Output: 0
print(solution.sumEvenDigits(10002)) # Output: 2
print(solution.sumEvenDigits(99999)) # Output: 0

```