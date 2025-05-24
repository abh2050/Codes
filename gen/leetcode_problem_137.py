```python
'''
# Sum of Even Digits
# Difficulty: Easy

# Problem Description:
# Given a non-negative integer num, return the sum of all its even digits.

# Examples:
# Example 1:
# Input: num = 2468
# Output: 20
# Explanation: The even digits are 2, 4, 6, and 8. Their sum is 2 + 4 + 6 + 8 = 20.

# Example 2:
# Input: num = 1357
# Output: 0
# Explanation: There are no even digits in the given number.

# Example 3:
# Input: num = 12345
# Output: 6
# Explanation: The even digits are 2 and 4. Their sum is 2 + 4 = 6.

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
        num_str = str(num)

        # Iterate through each digit (as a string) in the number
        for digit in num_str:
            digit_int = int(digit)
            # Check if the digit is even
            if digit_int % 2 == 0:
                sum_of_evens += digit_int

        return sum_of_evens


# Time Complexity: O(log(n)), where n is the input number. The number of digits in a number is proportional to its logarithm.
# Space Complexity: O(1), as we are using a constant amount of extra space.


# Test Cases
solution = Solution()
print(solution.sumEvenDigits(2468))  # Output: 20
print(solution.sumEvenDigits(1357))  # Output: 0
print(solution.sumEvenDigits(12345)) # Output: 6
print(solution.sumEvenDigits(0))  # Output: 0
print(solution.sumEvenDigits(102040)) # Output: 6

```