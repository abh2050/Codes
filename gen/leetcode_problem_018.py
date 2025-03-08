```python
'''
# Longest Substring with Unique Characters and at Most K Repeating Characters

# Difficulty: Medium

# Problem Description:
# Given a string s, find the length of the longest substring that contains only unique characters, 
# with the exception that at most one character can repeat up to k times.

# Examples:
# Example 1:
# Input: s = "aabacbebebe", k = 2
# Output: 7
# Explanation: The longest substring is "aabacbe" with length 7. 'b' repeats 2 times (<=k), while all other characters are unique.

# Example 2:
# Input: s = "aabbc", k = 1
# Output: 3
# Explanation: The longest substring is "aab" or "bbc" with length 3.

# Example 3:
# Input: s = "abcabcbb", k = 2
# Output: 3
# Explanation: "abc" is the longest substring with all unique characters.

# Constraints:
# 1 <= s.length <= 10^4
# 0 <= k <= s.length
# s consists of lowercase English letters.
'''

from collections import defaultdict

class Solution:
    def longestSubstringWithKRepeating(self, s: str, k: int) -> int:
        """
        Finds the length of the longest substring with unique characters and at most k repeating characters.

        Args:
            s: The input string.
            k: The maximum allowed repetitions for a single character.

        Returns:
            The length of the longest substring.
        """
        n = len(s)
        max_len = 0
        for i in range(n):
            char_counts = defaultdict(int)
            repeating_char = None
            repeating_count = 0
            for j in range(i, n):
                char_counts[s[j]] += 1
                if char_counts[s[j]] > 1 and (repeating_char is None or s[j] == repeating_char):  # Track repeating char
                    repeating_char = s[j]
                    repeating_count = char_counts[s[j]]
                elif char_counts[s[j]] > 1 and s[j] != repeating_char: # More than one character repeating, break
                    break

                if repeating_char is None or repeating_count <= k:  # Valid substring condition
                    max_len = max(max_len, j - i + 1)
                else: # Repeating char exceeds limit
                    break


        return max_len

# Time Complexity: O(n^2),  Nested loops to iterate through all possible substrings.
# Space Complexity: O(1), Constant extra space for the character count dictionary (limited to 26 lowercase letters)


# Test Cases
solution = Solution()

# Example 1
s1 = "aabacbebebe"
k1 = 2
print(f"Input: s = '{s1}', k = {k1}")
print(f"Output: {solution.longestSubstringWithKRepeating(s1, k1)}\n")  # Output: 7

# Example 2
s2 = "aabbc"
k2 = 1
print(f"Input: s = '{s2}', k = {k2}")
print(f"Output: {solution.longestSubstringWithKRepeating(s2, k2)}\n")  # Output: 3

# Example 3
s3 = "abcabcbb"
k3 = 2
print(f"Input: s = '{s3}', k = {k3}")
print(f"Output: {solution.longestSubstringWithKRepeating(s3, k3)}\n")  # Output: 3


# Example 4 - Added for clarity
s4 = "aaabbbccc"
k4 = 1
print(f"Input: s = '{s4}', k = {k4}")
print(f"Output: {solution.longestSubstringWithKRepeating(s4, k4)}\n") # Output 2

# Example 5 - Added for clarity
s5 = ""
k5 = 0
print(f"Input: s = '{s5}', k = {k5}")
print(f"Output: {solution.longestSubstringWithKRepeating(s5, k5)}\n") # Output 0

# Example 6 - Added for clarity
s6 = "a"
k6 = 1
print(f"Input: s = '{s6}', k = {k6}")
print(f"Output: {solution.longestSubstringWithKRepeating(s6, k6)}\n") # Output 1
```