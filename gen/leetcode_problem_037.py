```python
'''
# Sum of Even Digits
# Difficulty: Easy

# Problem Description:
# Given a non-negative integer num, return the sum of all its even digits.

# Examples:
# Example 1:
# Input: num = 246
# Output: 12
# Explanation: The even digits are 2, 4, and 6. Their sum is 2 + 4 + 6 = 12.

# Example 2:
# Input: num = 1357
# Output: 0
# Explanation: There are no even digits in the number.

# Example 3:
# Input: num = 0
# Output: 0
# Explanation: The only digit is 0, which is even, so the sum is 0.

# Constraints:
# 0 <= num <= 10^9
'''

class Solution:
    def sumEvenDigits(self, num: int) -> int:
        """
        Calculates the sum of even digits in a given integer.

        Args:
            num: The non-negative integer.

        Returns:
            The sum of even digits.
        """

        sum_of_evens = 0
        for digit_char in str(num):  # Convert to string for easy digit access
            digit = int(digit_char)
            if digit % 2 == 0:
                sum_of_evens += digit

        return sum_of_evens


# Time Complexity: O(log n) - where n is the input number. The number of digits is proportional to log base 10 of n.
# Space Complexity: O(1) - We are using a constant amount of extra space.


# Test Cases
solution = Solution()
print(solution.sumEvenDigits(246))  # Output: 12
print(solution.sumEvenDigits(1357))  # Output: 0
print(solution.sumEvenDigits(0))  # Output: 0
print(solution.sumEvenDigits(1024)) # Output: 6
print(solution.sumEvenDigits(9999)) # Output: 0
print(solution.sumEvenDigits(2222)) # Output: 8
```