```python
'''
# Sum of Even Digits
# Difficulty: Easy

# Problem Description:
# Given a non-negative integer num, return the sum of all its even digits.

# Examples:
# Example 1:
# Input: num = 1234
# Output: 6
# Explanation: The even digits are 2 and 4. Their sum is 2 + 4 = 6.

# Example 2:
# Input: num = 579
# Output: 0
# Explanation: There are no even digits.

# Example 3:
# Input: num = 2468
# Output: 20
# Explanation: The even digits are 2, 4, 6, and 8. Their sum is 2 + 4 + 6 + 8 = 20.

# Constraints:
# 0 <= num <= 10^9
'''

class Solution:
    def sumEvenDigits(self, num: int) -> int:
        """
        Calculates the sum of even digits in a non-negative integer.

        Args:
            num: The input non-negative integer.

        Returns:
            The sum of even digits.
        """

        sum_of_evens = 0
        for digit in str(num):  # Convert to string for easy iteration
            digit = int(digit)
            if digit % 2 == 0:
                sum_of_evens += digit

        return sum_of_evens

# Time Complexity: O(log(n)), where n is the input number. The number of digits is proportional to log10(n).
# Space Complexity: O(1), we are only using a few variables to store the sum and digits, regardless of the input size.


# Test Cases
solution = Solution()
print(solution.sumEvenDigits(1234))  # Output: 6
print(solution.sumEvenDigits(579))   # Output: 0
print(solution.sumEvenDigits(2468))  # Output: 20
print(solution.sumEvenDigits(0))    # Output: 0
print(solution.sumEvenDigits(100002)) # Output: 2
print(solution.sumEvenDigits(99999)) # Output: 0

```