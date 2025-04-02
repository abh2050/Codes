```python
'''
# Check for Even Digits
# Difficulty: Easy

# Problem Description:
# Given a non-negative integer num, return True if num contains only even digits, and False otherwise.
# Note: 0 is considered an even digit.

# Examples:
# Example 1:
# Input: num = 2468
# Output: True
# Explanation: All digits (2, 4, 6, 8) are even.

# Example 2:
# Input: num = 3224
# Output: False
# Explanation: The digit 3 is odd.

# Example 3:
# Input: num = 0
# Output: True
# Explanation: 0 is considered an even digit.


# Constraints:
# 0 <= num <= 10^9
'''

class Solution:
    def hasEvenDigitsOnly(self, num: int) -> bool:
        """
        Checks if a number contains only even digits.

        Args:
            num: The non-negative integer to check.

        Returns:
            True if the number contains only even digits, False otherwise.
        """

        # Convert the number to a string to easily iterate through its digits
        num_str = str(num)

        # Iterate through each digit in the string
        for digit in num_str:
            # Convert the digit back to an integer
            digit_int = int(digit)

            # Check if the digit is odd
            if digit_int % 2 != 0:
                return False  # If an odd digit is found, return False immediately

        # If the loop completes without finding any odd digits, return True
        return True


# Time Complexity: O(log(n)), where n is the input number. The number of digits in a number is proportional to log(n).
# Space Complexity: O(log(n)), as we convert the number to a string, the space used is proportional to the number of digits.


# Test cases
solution = Solution()
print(solution.hasEvenDigitsOnly(2468))  # Output: True
print(solution.hasEvenDigitsOnly(3224))  # Output: False
print(solution.hasEvenDigitsOnly(0))  # Output: True
print(solution.hasEvenDigitsOnly(1024))  # Output: False
print(solution.hasEvenDigitsOnly(88888)) # Output: True
print(solution.hasEvenDigitsOnly(24680)) # Output: True
```