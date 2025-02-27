class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        Checks if a string can be a palindrome after deleting at most one character.

        Args:
            s: The input string.

        Returns:
            True if the string can be a palindrome after deleting at most one character, False otherwise.
        """

        def is_palindrome(sub_s):
            """Helper function to check if a string is a palindrome."""
            left, right = 0, len(sub_s) - 1
            while left < right:
                if sub_s[left] != sub_s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                # Try deleting the left character or the right character
                return is_palindrome(s[left+1:right+1]) or is_palindrome(s[left:right])
            left += 1
            right -= 1

        return True  # String is already a palindrome

# Example Usage (and testing)
if __name__ == '__main__':
    sol = Solution()

    # Test cases
    print(f"aba: {sol.validPalindrome('aba')}")  # Expected: True
    print(f"abca: {sol.validPalindrome('abca')}")  # Expected: True
    print(f"abcda: {sol.validPalindrome('abcda')}")  # Expected: False
    print(f"deeee: {sol.validPalindrome('deeee')}") #Expected: True
    print(f"eeeee: {sol.validPalindrome('eeeee')}") #Expected: True
    print(f"acxzca: {sol.validPalindrome('acxzca')}") # Expected: True
    print(f"aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupucnlmglmgqvfqnvgbtapekouga: {sol.validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupucnlmglmgqvfqnvgbtapekouga")}") # Expected: True
