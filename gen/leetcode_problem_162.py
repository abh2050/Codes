```python
'''
# Check for Alternating Parity
# Difficulty: Easy

# Problem Description:
# Given a non-negative integer n, return True if the digits of n alternate between even and odd, and False otherwise.  The first digit can be either even or odd.  A single-digit number always returns True.

# Examples:
# Example 1:
# Input: n = 123
# Output: True
# Explanation: 1 is odd, 2 is even, 3 is odd.  The digits alternate parity.

# Example 2:
# Input: n = 241
# Output: False
# Explanation: 2 is even, 4 is even, 1 is odd. The parity doesn't alternate.

# Example 3:
# Input: n = 7
# Output: True
# Explanation: Single digit numbers always return True.


# Constraints:
# 0 <= n <= 2 * 10^9 
'''

class Solution:
    def alternatingParity(self, n: int) -> bool:
        """
        Checks if the digits of n alternate in parity.

        Args:
            n: The non-negative integer.

        Returns:
            True if the digits alternate parity, False otherwise.
        """
        s = str(n)
        if len(s) <= 1:
            return True

        for i in range(1, len(s)):
            prev_digit_parity = int(s[i-1]) % 2
            curr_digit_parity = int(s[i]) % 2
            if prev_digit_parity == curr_digit_parity:
                return False
        return True

# Time Complexity: O(log n) - because the number of digits in n is proportional to log n.
# Space Complexity: O(log n) - due to the string conversion, which creates a string with length proportional to log n.


# Test Cases
sol = Solution()
print(f"Input: 123, Output: {sol.alternatingParity(123)}, Expected: True")  # True
print(f"Input: 241, Output: {sol.alternatingParity(241)}, Expected: False") # False
print(f"Input: 7, Output: {sol.alternatingParity(7)}, Expected: True")     # True
print(f"Input: 12345, Output: {sol.alternatingParity(12345)}, Expected: True")  # True
print(f"Input: 224466, Output: {sol.alternatingParity(224466)}, Expected: False") # False
print(f"Input: 0, Output: {sol.alternatingParity(0)}, Expected: True")  # True
print(f"Input: 10101, Output: {sol.alternatingParity(10101)}, Expected: True") # True
print(f"Input: 20202, Output: {sol.alternatingParity(20202)}, Expected: False") # False


```