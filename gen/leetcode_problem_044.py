```python
'''
# Check for Even Digits
# Difficulty: Easy

# Problem Description:
# Given an integer num, return True if all the digits in the integer are even, and False otherwise.

# Examples:
# Example 1:
# Input: num = 2468
# Output: True
# Explanation: All digits are even (2, 4, 6, 8).

# Example 2:
# Input: num = 3468
# Output: False
# Explanation: Digit 3 is odd.

# Example 3:
# Input: num = 0
# Output: True
# Explanation: 0 is considered even.

# Constraints:
# 0 <= num <= 10^6 
'''

class Solution:
    def areDigitsEven(self, num: int) -> bool:
        """
        Checks if all digits of a given integer are even.

        Args:
            num: The input integer.

        Returns:
            True if all digits are even, False otherwise.
        """

        # Convert the integer to a string for easier digit access
        num_str = str(num)

        # Iterate through each digit (character) in the string
        for digit in num_str:
            # Convert the digit back to an integer to check for evenness
            if int(digit) % 2 != 0:
                return False  # If any digit is odd, return False immediately

        return True # If all digits are even, return True

# Time Complexity: O(log(n)), where n is the input number. The number of digits is logarithmic to the value of the number.
# Space Complexity: O(log(n)),  due to the string conversion. Technically O(1) if modifying the input directly is permitted. 


# Test Cases
solution = Solution()
print(solution.areDigitsEven(2468))  # Output: True
print(solution.areDigitsEven(3468))  # Output: False
print(solution.areDigitsEven(0))   # Output: True
print(solution.areDigitsEven(102))  # Output: False
print(solution.areDigitsEven(2460)) # Output: True
print(solution.areDigitsEven(1000000)) # Output: False

```