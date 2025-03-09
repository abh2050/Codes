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
# Explanation: The even digits are 2 and 4, their sum is 6.

# Example 2:
# Input: num = 579
# Output: 0
# Explanation: There are no even digits in the input number.


# Constraints:
# 0 <= num <= 10^9
'''

class Solution:
    def sumEvenDigits(self, num: int) -> int:
        """
        Calculates the sum of even digits in a given integer.

        Args:
            num: The input non-negative integer.

        Returns:
            The sum of even digits.
        """
        sum_of_evens = 0
        for digit in str(num):  # Convert to string to iterate through digits
            digit = int(digit)
            if digit % 2 == 0:
                sum_of_evens += digit
        return sum_of_evens

# Time Complexity: O(log(n)), where n is the input number. We iterate through the digits, 
# and the number of digits is proportional to the logarithm of the number.
# Space Complexity: O(1) - We use constant extra space.


# Test Cases
solution = Solution()
print(solution.sumEvenDigits(1234))  # Output: 6
print(solution.sumEvenDigits(579))   # Output: 0
print(solution.sumEvenDigits(2468))  # Output: 20
print(solution.sumEvenDigits(13579)) # Output: 0
print(solution.sumEvenDigits(0))     # Output: 0
print(solution.sumEvenDigits(1000000002)) # Output: 2


```