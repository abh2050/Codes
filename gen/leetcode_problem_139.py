```python
'''
# Check for Even Digits
# Difficulty: Easy

# Problem Description:
# Given an integer n, return True if all the digits of n are even, otherwise return False.

# Examples:
# Example 1:
# Input: n = 2468
# Output: True
# Explanation: All digits (2, 4, 6, 8) are even.

# Example 2:
# Input: n = 3224
# Output: False
# Explanation: The digit 3 is odd.

# Example 3:
# Input: n = 0
# Output: True
# Explanation: 0 is considered an even digit.

# Constraints:
# 0 <= n <= 10^9
'''

class Solution:
    def areDigitsEven(self, n: int) -> bool:
        """
        Checks if all digits of an integer are even.

        Args:
            n: The integer to check.

        Returns:
            True if all digits are even, False otherwise.
        """

        # Convert the integer to a string to easily iterate through digits
        n_str = str(n)

        # Iterate through each digit in the string
        for digit in n_str:
            # Convert the digit back to an integer
            digit_int = int(digit)

            # Check if the digit is odd. If it is, return False immediately.
            if digit_int % 2 != 0:
                return False

        # If the loop completes without finding an odd digit, return True.
        return True


# Time Complexity: O(log n) - The number of digits in n is proportional to log n.
# Space Complexity: O(log n) -  Storing the string representation of n takes space proportional to the number of digits, which is O(log n). Could be O(1) if we directly operate on the integer with repeated division by 10.


# Test cases
solution = Solution()
print(solution.areDigitsEven(2468))  # Output: True
print(solution.areDigitsEven(3224))  # Output: False
print(solution.areDigitsEven(0))  # Output: True
print(solution.areDigitsEven(102)) # Output: False
print(solution.areDigitsEven(220)) # Output: True
print(solution.areDigitsEven(88888)) # Output: True
print(solution.areDigitsEven(99999)) # Output: False


```