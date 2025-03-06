def minRemoveToMakeValid(s: str) -> str:
    """
    Removes the minimum number of parentheses to make a string valid.

    Args:
        s: The input string.

    Returns:
        A valid parentheses string with the minimum number of removals.
    """

    stack = []
    indices_to_remove = set()  # Use a set for efficient removal

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)  # Store the index
        elif char == ')':
            if stack:
                stack.pop()  # Matching parentheses, remove from stack
            else:
                indices_to_remove.add(i) #  Unmatched closing parenthesis, mark for removal

    # Add any remaining unmatched open parentheses in the stack to the removal set
    indices_to_remove.update(stack)

    result = ""
    for i, char in enumerate(s):
        if i not in indices_to_remove:
            result += char

    return result


# Test Cases
test_cases = [
    ("lee(t(c)o)de)", "lee(t(c)o)de"),  # Example 1
    ("a)b(c)d", "ab(c)d"),  # Example 2
    ("))((", ""),  # Example 3
    ("))())", "()"),
    ("(a(b(c)d)", "a(b(c)d)"),
    ("a(b(c)d)", "a(b(c)d)"),
    ("())()((", "()()"),
    ("((()))", "((()))"),
    ("", ""),  # Empty string
    ("abc", "abc"), # No parentheses
    ("(", ""),      # Single unmatched opening
    (")", ""),      # Single unmatched closing
]

for input_str, expected_output in test_cases:
    actual_output = minRemoveToMakeValid(input_str)
    if actual_output == expected_output:
        print(f"Test Passed: Input = '{input_str}', Output = '{actual_output}'")
    else:
        print(f"Test Failed: Input = '{input_str}', Expected = '{expected_output}', Actual = '{actual_output}'")
