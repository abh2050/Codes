```python
'''
# Check for Even Digits
# Difficulty: Easy

# Problem Description:
# Given an integer n, return True if all the digits of n are even, and False otherwise.

# Examples:
# Example 1:
# Input: n = 2468
# Output: True
# Explanation: All digits (2, 4, 6, 8) are even.

# Example 2:
# Input: n = 24681
# Output: False
# Explanation: The digit 1 is odd.

# Example 3:
# Input: n = 0
# Output: True
# Explanation: 0 is considered an even digit.

# Constraints:
# 0 <= n <= 2**31 - 1 
'''

class Solution:
    def allEvenDigits(self, n: int) -> bool:
        """
        Checks if all digits of an integer are even.

        Args:
            n: The input integer.

        Returns:
            True if all digits are even, False otherwise.
        """

        # Convert the integer to a string for easy digit access
        n_str = str(n)

        # Iterate through each digit
        for digit in n_str:
            # Convert the digit back to an integer and check if it's even
            if int(digit) % 2 != 0:
                return False  # If any digit is odd, return False immediately

        return True # If all digits are even, return True

# Time Complexity: O(log n) - Number of digits in n is proportional to log n
# Space Complexity: O(log n) - String conversion uses space proportional to log n



# Test cases
solution = Solution()
print(solution.allEvenDigits(2468))  # Output: True
print(solution.allEvenDigits(24681)) # Output: False
print(solution.allEvenDigits(0))     # Output: True
print(solution.allEvenDigits(2460))  # Output: True
print(solution.allEvenDigits(1))     # Output: False
print(solution.allEvenDigits(102))   # Output: False


```