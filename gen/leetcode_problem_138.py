```python
'''
# Check for Alternating Parity
# Difficulty: Easy

# Problem Description:
# Given a list of non-negative integers, return True if the parity of the elements alternates 
# (i.e., even then odd then even, or odd then even then odd, etc.), and False otherwise. 
# An empty list is considered to have alternating parity.


# Examples:
# Example 1:
# Input: nums = [1, 2, 3, 4]
# Output: True
# Explanation: The parity alternates: odd, even, odd, even.

# Example 2:
# Input: nums = [2, 2, 3, 4]
# Output: False
# Explanation: The parity doesn't alternate at index 1 (even, even).

# Example 3:
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
            nums: A list of non-negative integers.

        Returns:
            True if the parity alternates, False otherwise.
        """

        n = len(nums)
        if n == 0:  # Handle empty list case.
            return True

        for i in range(n - 1):
            if nums[i] % 2 == nums[i + 1] % 2:
                return False  # Parity doesn't alternate.

        return True # Parity alternates throughout the list.


# Time Complexity: O(n) -  In the worst case, we iterate through the entire list once.
# Space Complexity: O(1) - We use constant extra space.



# Test Cases
sol = Solution()

print(f"Test case 1: {sol.alternatingParity([1, 2, 3, 4]) == True}")  # Output: True
print(f"Test case 2: {sol.alternatingParity([2, 2, 3, 4]) == False}") # Output: False
print(f"Test case 3: {sol.alternatingParity([]) == True}")  # Output: True
print(f"Test case 4: {sol.alternatingParity([1]) == True}")  # Output: True
print(f"Test case 5: {sol.alternatingParity([1,3,5]) == False}")  # Output: False
print(f"Test case 6: {sol.alternatingParity([2,4,6]) == False}")  # Output: False
print(f"Test case 7: {sol.alternatingParity([1,2,1,2]) == True}") # Output: True


```