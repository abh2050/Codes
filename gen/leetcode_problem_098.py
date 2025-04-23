```python
'''
# Check for Even Digits
# Difficulty: Easy

# Problem Description:
# Given an integer num, return True if all the digits in the number are even. Otherwise, return False.

# Examples:
# Example 1:
# Input: num = 2468
# Output: True
# Explanation: All digits are even: 2, 4, 6, 8.

# Example 2:
# Input: num = 3224
# Output: False
# Explanation: Digit 3 is odd.

# Example 3:
# Input: num = 0
# Output: True
# Explanation: 0 is an even digit.


# Constraints:
# 0 <= num <= 10^6
'''

class Solution:
    def allEvenDigits(self, num: int) -> bool:
        """
        Checks if all digits in a number are even.

        Args:
            num: The input integer.

        Returns:
            True if all digits are even, False otherwise.
        """

        # Convert the number to a string to iterate over digits
        num_str = str(num)

        for digit in num_str:
            # Convert the digit back to an integer to check for evenness
            if int(digit) % 2 != 0:
                return False  # Found an odd digit, so return False immediately

        return True  # All digits were even


# Time Complexity: O(log(n)), where n is the input number. The number of digits is proportional to the logarithm of n.
# Space Complexity: O(1), as we only use a few variables to store the string and digits.


# Test cases
solution = Solution()
print(solution.allEvenDigits(2468))  # Output: True
print(solution.allEvenDigits(3224))  # Output: False
print(solution.allEvenDigits(0))  # Output: True
print(solution.allEvenDigits(102)) # Output: False
print(solution.allEvenDigits(4444)) # Output: True
print(solution.allEvenDigits(2)) # Output: True
```