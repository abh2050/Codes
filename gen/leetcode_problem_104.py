```python
'''
# Check for Alternating Parity
# Difficulty: Easy

# Problem Description:
# Given a non-negative integer n, return True if the digits of n alternate in parity (even to odd or odd to even), and False otherwise.  The parity of a digit is whether it is even or odd.  A single digit number always returns True.

# Examples:
# Example 1:
# Input: n = 123
# Output: True
# Explanation: The digits alternate in parity: 1 (odd), 2 (even), 3 (odd).

# Example 2:
# Input: n = 122
# Output: False
# Explanation: The digits do not alternate in parity: 2 and 2 have the same parity.

# Example 3:
# Input: n = 5
# Output: True
# Explanation: A single digit always returns True.

# Constraints:
# 0 <= n <= 10^9 
'''

class Solution:
    def alternatingParity(self, n: int) -> bool:
        """
        Checks if the digits of a number alternate in parity.

        Args:
            n: The non-negative integer.

        Returns:
            True if the digits alternate in parity, False otherwise.
        """
        s = str(n)
        if len(s) <= 1:
            return True
        
        for i in range(len(s) - 1):
            if int(s[i]) % 2 == int(s[i+1]) % 2:
                return False
        return True
        

# Time Complexity: O(log n) - The number of digits in n is proportional to log n.
# Space Complexity: O(log n) -  Converting to a string takes space proportional to the number of digits. We could optimize to O(1) by working directly with the integer via division and modulo, but the string approach is cleaner for readability.

# Test Cases
print("Test Case 1:", Solution().alternatingParity(123))  # Output: True
print("Test Case 2:", Solution().alternatingParity(122))  # Output: False
print("Test Case 3:", Solution().alternatingParity(5))  # Output: True
print("Test Case 4:", Solution().alternatingParity(12345))  # Output: True
print("Test Case 5:", Solution().alternatingParity(2468))  # Output: False
print("Test Case 6:", Solution().alternatingParity(13579))  # Output: True
print("Test Case 7:", Solution().alternatingParity(0))  # Output: True

```