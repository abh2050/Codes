```python
'''
# Check for Balanced Parentheses Substring
# Difficulty: Easy

# Problem Description:
# Given a string s containing only '(' and ')', return the length of the longest balanced parentheses substring.

# Examples:
# Example 1:
# Input: s = "(()"
# Output: 2
# Explanation: The longest balanced parentheses substring is "()".

# Example 2:
# Input: s = ")()())"
# Output: 4
# Explanation: The longest balanced parentheses substring is "()()".

# Example 3:
# Input: s = ""
# Output: 0

# Constraints:
# 0 <= s.length <= 3 * 10^4
# s[i] is '(', or ')'.
'''

class Solution:
    def longestBalancedParentheses(self, s: str) -> int:
        """
        Finds the length of the longest balanced parentheses substring.

        Uses a stack to keep track of opening parentheses indices.
        Iterates through the string, pushing opening parentheses indices onto the stack.
        When a closing parenthesis is encountered, if the stack is not empty (meaning there's a matching opening parenthesis), 
        pop the top index from the stack and calculate the length of the balanced substring.
        If the stack is empty, it means the current closing parenthesis doesn't have a matching opening one.

        Time Complexity: O(n), where n is the length of the string s. We iterate through the string once.
        Space Complexity: O(n) in the worst case (all opening parentheses), for the stack.  
        """

        stack = []
        max_length = 0
        start = -1  # Initialize start index for balanced substring

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                    if stack:  # If stack is not empty, calculate length from the previous unmatched '('
                        max_length = max(max_length, i - stack[-1])
                    else:      # If stack is empty, calculate length from the beginning of the current balanced substring
                        max_length = max(max_length, i - start)
                else:
                    start = i  # Reset the start index for a balanced substring

        return max_length



# Test Cases
solution = Solution()

print(f"Input: '(()', Output: {solution.longestBalancedParentheses('(()')}, Expected: 2")
print(f"Input: ')()())', Output: {solution.longestBalancedParentheses(')()())')}, Expected: 4")
print(f"Input: '', Output: {solution.longestBalancedParentheses('')}, Expected: 0")
print(f"Input: '()(())', Output: {solution.longestBalancedParentheses('()(())')}, Expected: 6")
print(f"Input: '(()((()))', Output: {solution.longestBalancedParentheses('(()((()))')}, Expected: 8")
print(f"Input: ')(', Output: {solution.longestBalancedParentheses(')(')}, Expected: 0")
print(f"Input: '((((', Output: {solution.longestBalancedParentheses('((((')}, Expected: 0")
print(f"Input: '))))', Output: {solution.longestBalancedParentheses('))))')}, Expected: 0")

```