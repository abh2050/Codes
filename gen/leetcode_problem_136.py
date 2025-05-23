```python
'''
# Check for Even Digits
# Difficulty: Easy

# Problem Description:
# Given an integer num, return True if all the digits in the number are even, and False otherwise.

# Examples:
# Example 1:
# Input: num = 2468
# Output: True
# Explanation: All digits (2, 4, 6, 8) are even.

# Example 2:
# Input: num = 346
# Output: False
# Explanation: Digit 3 is odd.

# Example 3:
# Input: num = 0
# Output: True
# Explanation: 0 is considered an even digit.


# Constraints:
# 0 <= num <= 10^6
'''

class Solution:
    def areAllDigitsEven(self, num: int) -> bool:
        """
        Checks if all digits in a number are even.

        Args:
            num: The input integer.

        Returns:
            True if all digits are even, False otherwise.
        """

        # Convert the number to a string to easily access individual digits
        num_str = str(num)

        # Iterate through the digits
        for digit in num_str:
            # Convert digit back to integer for checking even/odd
            if int(digit) % 2 != 0:
                return False  # Found an odd digit, return False immediately

        return True  # All digits were even

# Time Complexity: O(log(n)), where n is the input number. In the worst case, we iterate through all the digits of the number. The number of digits is proportional to log base 10 of n.
# Space Complexity: O(log(n)), due to the string conversion.  This could be considered O(1) if the problem allowed modifying the input num directly.


# Test cases
sol = Solution()
print(sol.areAllDigitsEven(2468))  # Output: True
print(sol.areAllDigitsEven(346))  # Output: False
print(sol.areAllDigitsEven(0))  # Output: True
print(sol.areAllDigitsEven(102))  # Output: False
print(sol.areAllDigitsEven(2460))  # Output: True
print(sol.areAllDigitsEven(1000000)) # Output: False



```