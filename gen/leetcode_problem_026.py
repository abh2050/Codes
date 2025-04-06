```python
'''
# Check for Alternating Parity
# Difficulty: Easy

# Problem Description:
# Given a non-negative integer n, return True if the digits of n alternate in parity (even to odd or odd to even), and False otherwise.  The parity of a digit is its property of being even or odd.  A single-digit number is considered to have alternating parity.

# Examples:
# Example 1:
# Input: n = 123
# Output: True
# Explanation: The digits alternate between odd (1) and even (2), and then odd (3).

# Example 2:
# Input: n = 2244
# Output: False
# Explanation: The digits do not alternate in parity.

# Example 3:
# Input: n = 7
# Output: True
# Explanation: Single digit numbers are considered to have alternating parity.


# Constraints:
# 0 <= n <= 10^9
'''

class Solution:
    def hasAlternatingParity(self, n: int) -> bool:
        """
        Checks if the digits of a number alternate in parity.

        Args:
            n: The non-negative integer to check.

        Returns:
            True if the digits alternate in parity, False otherwise.
        """
        s = str(n)
        for i in range(len(s) - 1):
            if int(s[i]) % 2 == int(s[i+1]) % 2:
                return False
        return True
        
# Time Complexity: O(log n) - because the number of digits in n is proportional to log n.
# Space Complexity: O(log n) - to store the string representation of n.  Could be O(1) if we worked directly with the integer via division and modulo operations, though the code would be less clear.



# Test Cases
sol = Solution()
print(sol.hasAlternatingParity(123))  # Output: True
print(sol.hasAlternatingParity(2244)) # Output: False
print(sol.hasAlternatingParity(7))    # Output: True
print(sol.hasAlternatingParity(12))   # Output: True
print(sol.hasAlternatingParity(2468)) # Output: False
print(sol.hasAlternatingParity(1357)) # Output: True
print(sol.hasAlternatingParity(0))    # Output: True
print(sol.hasAlternatingParity(10101)) #Output: True
print(sol.hasAlternatingParity(22)) #Output: False

```