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
# Explanation: All digits (2, 4, 6, 8) are even.

# Example 2:
# Input: num = 1234
# Output: False
# Explanation: Digit 1 and 3 are odd, so the function returns False.

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

        # Convert the integer to a string to easily iterate through digits
        num_str = str(num)

        for digit in num_str:
            # Convert the digit back to an integer and check if it's even
            if int(digit) % 2 != 0:
                return False  # If any digit is odd, return False immediately

        return True  # If all digits are even, return True


# Time Complexity: O(log(n)), where n is the input number. The number of digits is proportional to the logarithm of the number.
# Space Complexity: O(log(n)), as we convert the number to a string, which takes space proportional to the number of digits.

# Test Cases
solution = Solution()

print(solution.areAllDigitsEven(2468))  # Output: True
print(solution.areAllDigitsEven(1234))  # Output: False
print(solution.areAllDigitsEven(0))  # Output: True
print(solution.areAllDigitsEven(24680)) # Output: True
print(solution.areAllDigitsEven(1024)) # Output: False
print(solution.areAllDigitsEven(2222)) # Output: True
```