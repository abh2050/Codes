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
# Input: n = 1234
# Output: False
# Explanation: Digit 1 and 3 are odd.

# Example 3:
# Input: n = 0
# Output: True
# Explanation: 0 is considered even.


# Constraints:
# 0 <= n <= 10^9
'''

class Solution:
    def areDigitsEven(self, n: int) -> bool:
        """
        Checks if all digits of a given integer are even.

        Args:
            n: The integer to check.

        Returns:
            True if all digits are even, False otherwise.
        """

        # Convert the integer to a string to easily iterate through digits
        s = str(n)

        # Iterate through each digit (character) in the string
        for digit in s:
            # Convert the digit back to an integer
            d = int(digit)
            # If any digit is odd, return False immediately
            if d % 2 != 0:
                return False

        # If the loop completes without finding any odd digits, return True
        return True

# Time Complexity: O(log n) -  The number of digits in n is proportional to log10(n).
# Space Complexity: O(log n) - Converting the integer to a string takes space proportional to the number of digits.  We can improve this to O(1) if we avoid string conversion.



# Test cases
solution = Solution()
print(solution.areDigitsEven(2468))  # Output: True
print(solution.areDigitsEven(1234))  # Output: False
print(solution.areDigitsEven(0))  # Output: True
print(solution.areDigitsEven(24680))  # Output: True
print(solution.areDigitsEven(1024))  # Output: False
print(solution.areDigitsEven(204))  # Output: True


#Improved Solution with O(1) space:

class SolutionOptimized:
    def areDigitsEven(self, n: int) -> bool:
        """
        Checks if all digits of a given integer are even without string conversion.

        Args:
            n: The integer to check.

        Returns:
            True if all digits are even, False otherwise.
        """

        if n == 0: return True #handle the zero case

        while n > 0:
            digit = n % 10
            if digit % 2 != 0:
                return False
            n //= 10

        return True

# Test cases for optimized solution (identical outputs expected)
solution_optimized = SolutionOptimized()
print(solution_optimized.areDigitsEven(2468))  # Output: True
print(solution_optimized.areDigitsEven(1234))  # Output: False
print(solution_optimized.areDigitsEven(0))  # Output: True
print(solution_optimized.areDigitsEven(24680))  # Output: True
print(solution_optimized.areDigitsEven(1024))  # Output: False
print(solution_optimized.areDigitsEven(204))  # Output: True



```