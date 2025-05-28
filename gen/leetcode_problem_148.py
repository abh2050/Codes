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
# Explanation: 0 is considered an even digit.


# Constraints:
# 0 <= n <= 10^9
'''

class Solution:
    def areAllDigitsEven(self, n: int) -> bool:
        """
        Checks if all digits in an integer are even.

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
            # Check if the digit is odd. If odd, return False immediately.
            if digit_int % 2 != 0:
                return False
        
        # If the loop completes without finding an odd digit, all digits are even.
        return True


# Test Cases
solution = Solution()
print(solution.areAllDigitsEven(2468))  # Output: True
print(solution.areAllDigitsEven(1234))  # Output: False
print(solution.areAllDigitsEven(0))  # Output: True
print(solution.areAllDigitsEven(24680))  # Output: True
print(solution.areAllDigitsEven(1024))  # Output: False



'''
Time Complexity: O(log10(n)) - The number of iterations in the loop is proportional to the number of digits in n, which is logarithmic to the base 10 of n.
Space Complexity: O(1) -  We're using a constant amount of extra space for the string conversion and the digit variable, regardless of the input size.  Even though we convert to a string, the length of that string is still related to log10(n), so it doesn't significantly change the space complexity analysis.
'''
```