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
        Calculates the sum of even digits in a non-negative integer.

        Args:
            num: The non-negative integer.

        Returns:
            The sum of even digits.
        """

        sum_of_evens = 0
        for digit in str(num):  # Convert to string to iterate through digits
            digit = int(digit)
            if digit % 2 == 0:
                sum_of_evens += digit

        return sum_of_evens

        # Time Complexity: O(log n) where n is the input number because we iterate through the digits, which are logarithmic to the number itself.
        # Space Complexity: O(1) since we only use a few variables to store the sum and digits.


# Test Cases
solution = Solution()

print(f"Input: 246, Output: {solution.sumEvenDigits(246)}, Expected: 12")  # Example 1
print(f"Input: 1357, Output: {solution.sumEvenDigits(1357)}, Expected: 0")  # Example 2
print(f"Input: 0, Output: {solution.sumEvenDigits(0)}, Expected: 0")  # Example 3
print(f"Input: 1024, Output: {solution.sumEvenDigits(1024)}, Expected: 6") # Additional Test Case
print(f"Input: 9999, Output: {solution.sumEvenDigits(9999)}, Expected: 0") # Additional Test Case

```