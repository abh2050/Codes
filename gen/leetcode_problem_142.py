```python
'''
# Check for Alternating Parity
# Difficulty: Easy

# Problem Description:
# Given a list of integers, return True if the parity of the elements alternates, 
# otherwise return False.  The parity of an element is whether it's even or odd.
# An empty list or a list with a single element is considered to have alternating parity.

# Examples:
# Example 1:
# Input: nums = [1, 2, 3, 4]
# Output: True
# Explanation: The parity alternates: odd, even, odd, even.

# Example 2:
# Input: nums = [2, 2, 3, 4]
# Output: False
# Explanation: The parity does not alternate at index 1 (even, even).


# Example 3:
# Input: nums = [1]
# Output: True
# Explanation: A single element list is considered alternating.

# Constraints:
# 0 <= len(nums) <= 1000
# 0 <= nums[i] <= 1000
'''

class Solution:
    def alternatingParity(self, nums: list[int]) -> bool:
        """
        Checks if the parity of elements in a list alternates.

        Args:
            nums: A list of integers.

        Returns:
            True if parity alternates, False otherwise.
        """
        n = len(nums)
        if n <= 1:
            return True

        for i in range(n - 1):
            if (nums[i] % 2) == (nums[i+1] % 2):  # Check if adjacent elements have the same parity
                return False

        return True

# Time Complexity: O(N), where N is the length of the input list. We iterate through the list once.
# Space Complexity: O(1), as we use only constant extra space.


# Test Cases
solution = Solution()
print(solution.alternatingParity([1, 2, 3, 4]))  # Output: True
print(solution.alternatingParity([2, 2, 3, 4]))  # Output: False
print(solution.alternatingParity([1]))  # Output: True
print(solution.alternatingParity([]))  # Output: True
print(solution.alternatingParity([1, 3, 5]))  # Output: False
print(solution.alternatingParity([2, 4, 6]))  # Output: False
print(solution.alternatingParity([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # Output: True
print(solution.alternatingParity([1, 2, 2, 4, 5, 6])) # Output: False

```