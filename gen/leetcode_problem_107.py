```python
'''
# Count Vowels in a String
# Difficulty: Easy

# Problem Description:
# Given a string `s` consisting of lowercase English letters, return the number of vowels in `s`.
# Vowels are 'a', 'e', 'i', 'o', and 'u'.

# Examples:
# Example 1:
# Input: s = "hello"
# Output: 2
# Explanation: The vowels in "hello" are 'e' and 'o'.

# Example 2:
# Input: s = "leetcode"
# Output: 3
# Explanation: The vowels in "leetcode" are 'e', 'e', and 'o'.

# Example 3:
# Input: s = "rhythm"
# Output: 0
# Explanation: There are no vowels in "rhythm".


# Constraints:
# 1 <= s.length <= 1000
# s consists of lowercase English letters.
'''

class Solution:
    def countVowels(self, s: str) -> int:
        """
        Counts the number of vowels in a string.

        Args:
            s: The input string.

        Returns:
            The number of vowels in the string.
        """
        vowels = "aeiou"
        count = 0
        for char in s:
            if char in vowels:
                count += 1
        return count

        # Alternative solution using list comprehension:
        # return sum([1 for char in s if char in "aeiou"])

'''
Time Complexity: O(n), where n is the length of the string `s`. We iterate through the string once.
Space Complexity: O(1). We use constant extra space for the vowels string and the count variable. The list comprehension solution also has O(1) space complexity in practice because the generator doesn't materialize the entire list at once. 
'''


# Test cases
solution = Solution()
print(solution.countVowels("hello"))  # Output: 2
print(solution.countVowels("leetcode")) # Output: 3
print(solution.countVowels("rhythm"))  # Output: 0
print(solution.countVowels("aeiou")) # Output: 5
print(solution.countVowels("")) # Output: 0
print(solution.countVowels("b")) # Output: 0


```