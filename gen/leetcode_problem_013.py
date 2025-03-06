from collections import Counter

def minDeletions(s: str) -> int:
    """
    Calculates the minimum number of deletions required to make frequencies of characters in a string unique.

    Args:
        s: The input string.

    Returns:
        The minimum number of deletions required.
    """

    counts = Counter(s)
    frequencies = sorted(counts.values(), reverse=True)
    deletions = 0
    seen = set()

    for freq in frequencies:
        while freq > 0 and freq in seen:
            freq -= 1
            deletions += 1

        if freq > 0:
            seen.add(freq)

    return deletions

# Example Usage:
s1 = "aab"
print(f"Input: {s1}, Output: {minDeletions(s1)}")  # Output: 0

s2 = "aaabbbcc"
print(f"Input: {s2}, Output: {minDeletions(s2)}")  # Output: 2

s3 = "ceabaacb"
print(f"Input: {s3}, Output: {minDeletions(s3)}")  # Output: 2

s4 = "abcabc"
print(f"Input: {s4}, Output: {minDeletions(s4)}") # Output: 3
