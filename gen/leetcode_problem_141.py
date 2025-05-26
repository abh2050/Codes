```python
'''
# Check for Even Digits
# Difficulty: Easy

# Problem Description:
# Given an integer num, return True if all the digits in the number are even, otherwise return False.

# Examples:
# Example 1:
# Input: num = 2468
# Output: True
# Explanation: All digits are even: 2, 4, 6, and 8.

# Example 2:
# Input: num = 3224
# Output: False
# Explanation: The digit 3 is odd.

# Example 3:
# Input: num = 0
# Output: True
# Explanation: 0 is an even number.


# Constraints:
# 0 <= num <= 10^6
'''

class Solution:
    def checkEvenDigits(self, num: int) -> bool:
        """
        Checks if all digits in a number are even.

        Args:
            num: The integer to check.

        Returns:
            True if all digits are even, False otherwise.
        """

        # Convert the number to a string to iterate through digits
        num_str = str(num)

        for digit in num_str:
            # Convert the digit back to an integer to check for evenness
            if int(digit) % 2 != 0:
                return False  # Return False as soon as an odd digit is found

        return True  # If the loop completes without finding an odd digit, return True


# Time Complexity: O(log n) - where n is the input number. We iterate through the digits,
#                          which are proportional to the logarithm of the number.
# Space Complexity: O(log n) - due to the string conversion. Could be O(1) if we 
#                           handled it numerically using modulo and division, but
#                           string conversion makes the code cleaner/easier to read for an Easy problem.


# Test cases
solution = Solution()
print(solution.checkEvenDigits(2468))  # Output: True
print(solution.checkEvenDigits(3224))  # Output: False
print(solution.checkEvenDigits(0))    # Output: True
print(solution.checkEvenDigits(102))   # Output: False
print(solution.checkEvenDigits(2460)) # Output: True


```