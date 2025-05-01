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
# Explanation: The digit 1 is odd, so the function returns False.

# Example 3:
# Input: n = 0
# Output: True
# Explanation: 0 is considered an even digit.

# Constraints:
# 0 <= n <= 10^9 
'''

class Solution:
    def checkEvenDigits(self, n: int) -> bool:
        """
        Checks if all digits of an integer are even.

        Args:
            n: The integer to check.

        Returns:
            True if all digits are even, False otherwise.
        """

        # Convert the integer to a string for easy digit access
        s = str(n)

        # Iterate through each digit in the string
        for digit in s:
            # Convert the digit back to an integer
            d = int(digit)

            # Check if the digit is odd
            if d % 2 != 0:
                return False  # If an odd digit is found, return False immediately

        return True # If all digits are even, return True


# Time Complexity: O(log n) - The number of iterations is proportional to the number of digits in n, which is logarithmic with respect to n.
# Space Complexity: O(log n) -  Converting the integer to a string takes space proportional to the number of digits, which is logarithmic with respect to n.  Could be O(1) if we directly manipulate the integer using modulo and division.



# Test Cases
solution = Solution()
print(solution.checkEvenDigits(2468))  # Output: True
print(solution.checkEvenDigits(24681)) # Output: False
print(solution.checkEvenDigits(0))    # Output: True
print(solution.checkEvenDigits(2))    # Output: True
print(solution.checkEvenDigits(1))    # Output: False
print(solution.checkEvenDigits(1024)) # Output: False
print(solution.checkEvenDigits(2460)) # Output: True
```