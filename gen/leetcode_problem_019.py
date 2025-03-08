```python
'''
# Count Occurrences of a Character

# Difficulty: Easy

# Problem Description:
# Given a string `s` and a character `c`, return the number of times `c` appears in `s`.
# The comparison should be case-sensitive.

# Examples:
# Example 1:
# Input: s = "programming", c = "r"
# Output: 2
# Explanation: The character 'r' appears twice in the string "programming".

# Example 2:
# Input: s = "AbCdEfGh", c = "a"
# Output: 0
# Explanation: The character 'a' does not appear in the string "AbCdEfGh". Because the check is case sensitive 'a' is not the same as 'A'

# Example 3:
# Input: s = "banana", c = "a"
# Output: 3
# Explanation: The character 'a' appears thrice in the string "banana"

# Constraints:
# 1 <= len(s) <= 10^5
# c is a single character string.
'''

class Solution:
    def countOccurrences(self, s: str, c: str) -> int:
        """
        Counts the number of times a character appears in a string.

        Args:
            s: The input string.
            c: The character to count.

        Returns:
            The number of times the character appears in the string.
        """
        count = 0
        for char in s:
            if char == c:
                count += 1
        return count

        # Alternative one-liner solution using count():
        # return s.count(c)


# Time Complexity: O(n), where n is the length of the string s, as we iterate through the string once.
# Space Complexity: O(1), as we only use constant extra space.



# Test cases
solution = Solution()
print(solution.countOccurrences("programming", "r"))  # Output: 2
print(solution.countOccurrences("AbCdEfGh", "a"))  # Output: 0
print(solution.countOccurrences("banana", "a"))  # Output: 3
print(solution.countOccurrences("", "x")) # Output: 0
print(solution.countOccurrences("xxxxx", "x")) # Output: 5


```