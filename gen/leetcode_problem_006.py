def minWindowDistinctChars(s: str, chars: list[str]) -> str:
    """
    Finds the smallest substring of s that contains all the characters in chars at least once.

    Args:
        s: The input string.
        chars: A list of distinct characters.

    Returns:
        The smallest substring of s that contains all the characters in chars, or an empty string if no such substring exists.
    """

    if not chars:
        return ""

    char_count = {}
    for char in chars:
        char_count[char] = 0

    required = len(chars)
    formed = 0
    window_start = 0
    window_end = 0
    min_len = float('inf')
    result = ""

    while window_end < len(s):
        char = s[window_end]
        if char in char_count:
            char_count[char] += 1
            if char_count[char] == 1:
                formed += 1

        while formed == required:
            if (window_end - window_start + 1) < min_len:
                min_len = (window_end - window_start + 1)
                result = s[window_start : window_end + 1]

            left_char = s[window_start]
            if left_char in char_count:
                char_count[left_char] -= 1
                if char_count[left_char] == 0:
                    formed -= 1

            window_start += 1

        window_end += 1

    return result
