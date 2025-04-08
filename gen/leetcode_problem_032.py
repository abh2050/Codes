```python
'''
# Check for Even Digits
# Difficulty: Easy

# Problem Description:
# Given an integer num, return True if every digit in the number is even, and False otherwise.

# Examples:
# Example 1:
# Input: num = 2468
# Output: True
# Explanation: All digits are even: 2, 4, 6, 8.

# Example 2:
# Input: num = 1357
# Output: False
# Explanation: 1, 3, 5, and 7 are all odd digits.

# Example 3:
# Input: num = 24680
# Output: True
# Explanation: All digits are even: 2, 4, 6, 8, 0.

# Constraints:
# 0 <= num <= 10^6
'''

class Solution:
    def areDigitsEven(self, num: int) -> bool:
        """
        Checks if all digits of a number are even.

        Args:
            num: The input integer.

        Returns:
            True if all digits are even, False otherwise.
        """

        # Convert the number to a string to iterate through its digits
        num_str = str(num)

        # Iterate through each digit
        for digit in num_str:
            # Convert the digit back to an integer
            digit_int = int(digit)

            # If any digit is odd, return False
            if digit_int % 2 != 0:
                return False
        
        # If all digits are even, return True
        return True

# Time Complexity: O(log(n)), where n is the input number. The number of digits is proportional to the logarithm of the number.
# Space Complexity: O(log(n)), due to the string conversion.  We can also do this in O(1) space if we operate directly on the integer with division and modulo, but the string approach is arguably more readable for an "Easy" level problem.


# Test Cases
solution = Solution()
print(solution.areDigitsEven(2468))  # Output: True
print(solution.areDigitsEven(1357))  # Output: False
print(solution.areDigitsEven(24680)) # Output: True
print(solution.areDigitsEven(0))   # Output: True
print(solution.areDigitsEven(102))  # Output: False
print(solution.areDigitsEven(2222)) # Output: True

```