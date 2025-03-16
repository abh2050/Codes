```python
'''
# Check for Alternating Parity
# Difficulty: Easy

# Problem Description:
# Given a list of integers, determine if the parity (even or odd) of the elements alternates.  Return True if the parity alternates, False otherwise.  An empty list or a list with a single element is considered to have alternating parity.

# Examples:
# Example 1:
# Input: nums = [1, 2, 3, 4]
# Output: True
# Explanation: The parity alternates: odd, even, odd, even.

# Example 2:
# Input: nums = [2, 4, 6]
# Output: False
# Explanation: The parity does not alternate.

# Example 3:
# Input: nums = [1]
# Output: True
# Explanation: A single element list is considered alternating.

# Example 4:
# Input: nums = []
# Output: True
# Explanation: An empty list is considered alternating.

# Constraints:
# 0 <= len(nums) <= 1000
# 0 <= nums[i] <= 1000
'''

class Solution:
    def alternatingParity(self, nums: list[int]) -> bool:
        """
        Checks if the parity of elements in a list alternates.

        Args:
            nums: The input list of integers.

        Returns:
            True if the parity alternates, False otherwise.
        """
        n = len(nums)
        if n <= 1:
            return True

        for i in range(n - 1):
            if (nums[i] % 2) == (nums[i+1] % 2):  # Check if adjacent elements have the same parity
                return False

        return True  # Parity alternates throughout the list


# Time Complexity: O(n), where n is the length of the input list. We iterate through the list once.
# Space Complexity: O(1), constant extra space is used.

# Test Cases
sol = Solution()

print(sol.alternatingParity([1, 2, 3, 4]))  # Output: True
print(sol.alternatingParity([2, 4, 6]))  # Output: False
print(sol.alternatingParity([1]))  # Output: True
print(sol.alternatingParity([]))  # Output: True
print(sol.alternatingParity([1, 3, 5])) # Output: False
print(sol.alternatingParity([2, 4, 1, 3])) # Output: False
print(sol.alternatingParity([2, 1, 2, 1])) # Output: True
```