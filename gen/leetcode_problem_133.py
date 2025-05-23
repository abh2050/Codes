```python
'''
# Longest Substring with K Distinct Vowels
# Difficulty: Medium

# Problem Description:
# Given a string s consisting of lowercase English letters, return the length of the longest substring containing exactly k distinct vowels.
# Vowels are 'a', 'e', 'i', 'o', 'u'.

# Examples:
# Example 1:
# Input: s = "aeiouia", k = 3
# Output: 6
# Explanation: The substring "aeiouia" contains 3 distinct vowels ('a', 'e', 'i', 'o', 'u').

# Example 2:
# Input: s = "rhythms", k = 0 
# Output: 5
# Explanation: The substring "rhythms" contains 0 distinct vowels.

# Example 3:
# Input: s = "bbaeicou", k = 2
# Output: 4
# Explanation: The substring "baeic" contains 2 distinct vowels "a", "e", "i".

# Constraints:
# 1 <= s.length <= 10^5
# 0 <= k <= 5
'''

class Solution:
    def longestSubstringWithKVowels(self, s: str, k: int) -> int:
        """
        Finds the length of the longest substring with exactly k distinct vowels.

        Args:
            s: The input string.
            k: The number of distinct vowels required.

        Returns:
            The length of the longest substring.
        """

        n = len(s)
        max_len = 0

        for i in range(n):
            for j in range(i, n):
                substring = s[i:j+1]
                vowels = set()
                for char in substring:
                    if char in "aeiou":
                        vowels.add(char)

                if len(vowels) == k:
                    max_len = max(max_len, len(substring))

        return max_len


# Time Complexity: O(n^2) due to the nested loops iterating through all possible substrings.
# Space Complexity: O(1) as we use a set of constant size (at most 5) to store vowels.


# Test Cases
solution = Solution()

# Example 1
s1 = "aeiouia"
k1 = 3
print(f"Input: s = '{s1}', k = {k1}")
print(f"Output: {solution.longestSubstringWithKVowels(s1, k1)}")  # Expected Output: 6

# Example 2
s2 = "rhythms"
k2 = 0
print(f"Input: s = '{s2}', k = {k2}")
print(f"Output: {solution.longestSubstringWithKVowels(s2, k2)}")  # Expected Output: 5


# Example 3
s3 = "bbaeicou"
k3 = 2
print(f"Input: s = '{s3}', k = {k3}")
print(f"Output: {solution.longestSubstringWithKVowels(s3, k3)}")  # Expected Output: 4


# Example 4: Edge case with no vowels and k>0
s4 = "bbbbb"
k4 = 1
print(f"Input: s = '{s4}', k = {k4}")
print(f"Output: {solution.longestSubstringWithKVowels(s4, k4)}")  # Expected Output: 0

# Example 5: Edge case with empty string
s5 = ""
k5 = 2
print(f"Input: s = '{s5}', k = {k5}")
print(f"Output: {solution.longestSubstringWithKVowels(s5, k5)}")  # Expected Output: 0



```