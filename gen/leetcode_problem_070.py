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
# Explanation: The even digits are 2 and 4, and their sum is 6.

# Example 2:
# Input: num = 555
# Output: 0
# Explanation: There are no even digits in the number.

# Example 3:
# Input: num = 24680
# Output: 20
# Explanation: The even digits are 2, 4, 6, 8, and 0, and their sum is 20.

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
            The sum of the even digits.
        """

        sum_of_evens = 0
        for digit in str(num):  # Convert to string to iterate through digits
            digit = int(digit)
            if digit % 2 == 0:
                sum_of_evens += digit

        return sum_of_evens

        # Time Complexity: O(log(n)), where n is the input number. 
        # The number of digits in a number is proportional to the logarithm of the number.
        # Space Complexity: O(1). We are using a constant amount of extra space.


# Test cases
solution = Solution()
print(solution.sumEvenDigits(1234))  # Output: 6
print(solution.sumEvenDigits(555))  # Output: 0
print(solution.sumEvenDigits(24680))  # Output: 20
print(solution.sumEvenDigits(0))  # Output: 0
print(solution.sumEvenDigits(1000000001)) # Output: 0
print(solution.sumEvenDigits(22222)) # Output: 10
```