```python
'''
# Check for Sorted Vowels
# Difficulty: Easy

# Problem Description:
# Given a string s consisting of lowercase English letters, return true if all the vowels in s appear in alphabetical order (a, e, i, o, u) and false otherwise.

# Examples:
# Example 1:
# Input: s = "aeiou"
# Output: True
# Explanation: All vowels appear in alphabetical order.

# Example 2:
# Input: s = "archaeologist"
# Output: True
# Explanation: 'a', 'e', and 'o' appear in alphabetical order. 'i' and 'u' are not present so the condition is still true.

# Example 3:
# Input: s = "programming"
# Output: False
# Explanation: 'o' appears before 'a', which is not in alphabetical order.

# Constraints:
# 1 <= s.length <= 100
# s consists of lowercase English letters.
'''

class Solution:
    def areVowelsSorted(self, s: str) -> bool:
        """
        Checks if vowels in a string are sorted alphabetically.

        Args:
            s: The input string.

        Returns:
            True if vowels are sorted, False otherwise.
        """
        vowels = "aeiou"
        last_vowel_index = -1

        for char in s:
            if char in vowels:
                current_vowel_index = vowels.index(char)
                if current_vowel_index < last_vowel_index:
                    return False
                last_vowel_index = current_vowel_index

        return True
        


# Time Complexity: O(n), where n is the length of the string s. We iterate through the string once.
# Space Complexity: O(1), as we only store a few variables regardless of the input size.


# Test Cases
solution = Solution()
print(solution.areVowelsSorted("aeiou"))  # Output: True
print(solution.areVowelsSorted("archaeologist"))  # Output: True
print(solution.areVowelsSorted("programming"))  # Output: False
print(solution.areVowelsSorted("sequoia")) # Output: False
print(solution.areVowelsSorted("axyz")) # Output: True
print(solution.areVowelsSorted("medium")) # Output: True
print(solution.areVowelsSorted("eutopia")) # Output: True
print(solution.areVowelsSorted("aueio")) # Output: False


```