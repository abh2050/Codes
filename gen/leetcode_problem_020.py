```python
'''
# Check for Balanced Parentheses in a Substring
# Difficulty: Easy

# Problem Description:
# Given a string containing only parentheses '(', ')', '{', '}', '[' and ']', 
# determine if a substring defined by start and end indices (inclusive) has balanced parentheses.
# Return True if the substring has balanced parentheses, False otherwise.


# Examples:
# Example 1:
# Input: s = "{([])}", start = 0, end = 5
# Output: True
# Explanation: The substring from index 0 to 5 is "{([])}", which is balanced.

# Example 2:
# Input: s = "[{]}", start = 0, end = 3
# Output: False
# Explanation: The substring from index 0 to 3 is "[{]}", which is not balanced.

# Example 3:
# Input: s = "()", start = 0, end = 1
# Output: True

# Constraints:
# 1 <= s.length <= 10^4
# 0 <= start <= end < s.length
# s[i] is one of '(', ')', '{', '}', '[' and ']'.
'''

class Solution:
    def isBalanced(self, s: str, start: int, end: int) -> bool:
        """
        Checks if a substring has balanced parentheses.

        Args:
            s: The input string.
            start: The start index of the substring (inclusive).
            end: The end index of the substring (inclusive).

        Returns:
            True if the substring is balanced, False otherwise.
        """
        stack = []
        matching = {')': '(', '}': '{', ']': '['}

        for i in range(start, end + 1):
            char = s[i]
            if char in matching:  # Closing parenthesis
                if not stack or stack.pop() != matching[char]:
                    return False
            elif char in matching.values():  # Opening parenthesis
                stack.append(char)
        
        return not stack # Return True if the stack is empty (all parentheses matched)



# Test Cases
solution = Solution()
print(solution.isBalanced("{([])}", 0, 5))  # Output: True
print(solution.isBalanced("[{]}", 0, 3))  # Output: False
print(solution.isBalanced("()", 0, 1)) # Output: True
print(solution.isBalanced("([)]", 0, 3)) # Output: False
print(solution.isBalanced("{[}]", 0, 3)) # Output: False
print(solution.isBalanced("([])", 0,2)) # Output: False
print(solution.isBalanced("([]{})", 1, 4))  # Output: True


'''
Time Complexity: O(n), where n is the length of the substring (end - start + 1). We iterate through the substring once.
Space Complexity: O(n) in the worst case, where the substring contains only opening parentheses and the stack stores all of them. 
'''
```