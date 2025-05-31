```python
'''
# Sum of Even Digits
# Difficulty: Easy

# Problem Description:
# Given a non-negative integer num, return the sum of its even digits.

# Examples:
# Example 1:
# Input: num = 1234
# Output: 6
# Explanation: The even digits are 2 and 4. Their sum is 2 + 4 = 6.

# Example 2:
# Input: num = 357
# Output: 0
# Explanation: There are no even digits in the given number.

# Example 3:
# Input: num = 24680
# Output: 20
# Explanation: The even digits are 2, 4, 6, 8 and 0. Their sum is 2 + 4 + 6 + 8 + 0 = 20.

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
        # Time Complexity: O(log n) -  Number of digits is proportional to log10(n)
        # Space Complexity: O(1) - Constant extra space is used.


# Test Cases
solution = Solution()

print(f"Input: 1234, Output: {solution.sumEvenDigits(1234)}, Expected: 6")
print(f"Input: 357, Output: {solution.sumEvenDigits(357)}, Expected: 0")
print(f"Input: 24680, Output: {solution.sumEvenDigits(24680)}, Expected: 20")
print(f"Input: 0, Output: {solution.sumEvenDigits(0)}, Expected: 0")
print(f"Input: 1000000000, Output: {solution.sumEvenDigits(1000000000)}, Expected: 0")


```