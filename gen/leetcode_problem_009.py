class Solution:
    def shortestPalindrome(self, s: str) -> str:
        """
        Finds the shortest palindrome by adding characters to the beginning of the string.

        Args:
            s: The input string.

        Returns:
            The shortest palindrome.
        """
        n = len(s)
        rev_s = s[::-1]
        for i in range(n):
            if s[:n-i] == rev_s[i:]:
                return rev_s[:i] + s
        return ""  # Should not happen based on problem constraints, but good practice

# Example usage
if __name__ == '__main__':
    sol = Solution()
    s1 = "aacecaaa"
    s2 = "abcd"
    s3 = "aba"

    print(f"shortestPalindrome('{s1}') = {sol.shortestPalindrome(s1)}")  # Output: aaacecaaa
    print(f"shortestPalindrome('{s2}') = {sol.shortestPalindrome(s2)}")  # Output: dcbabcd
    print(f"shortestPalindrome('{s3}') = {sol.shortestPalindrome(s3)}")  # Output: aba
