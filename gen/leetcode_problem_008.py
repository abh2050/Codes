from collections import Counter

def findAnagrams(s: str, p: str) -> list[int]:
    """
    Finds all start indices of p's anagrams in s.

    Args:
        s: The string to search in.
        p: The string to find anagrams of.

    Returns:
        A list of start indices of anagrams.
    """

    n = len(s)
    m = len(p)
    if m > n:
        return []

    p_count = Counter(p)
    window_count = Counter()
    result = []

    for i in range(n):
        # Add the current character to the window
        window_count[s[i]] += 1

        # If the window size exceeds p's length, remove the leftmost character
        if i >= m:
            window_count[s[i - m]] -= 1
            if window_count[s[i - m]] == 0:
                del window_count[s[i - m]]  # remove entry when the count reaches zero

        # Check if the current window is an anagram of p
        if window_count == p_count:
            result.append(i - m + 1)

    return result
