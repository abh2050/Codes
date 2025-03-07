```python
'''
# Check for Duplicates in a Sorted Array
# Difficulty: Easy

# Problem Description:
# Given a sorted array of integers `nums`, return `True` if any value appears at least twice in the array, and return `False` if every element is distinct.

# Examples:
# Example 1:
# Input: nums = [1,2,3,4,5]
# Output: False
# Explanation: No value appears more than once.

# Example 2:
# Input: nums = [1,1,2,3,4]
# Output: True
# Explanation: The value 1 appears twice.


# Constraints:
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
'''

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        Checks if a sorted array contains duplicate values.

        Args:
            nums: A sorted list of integers.

        Returns:
            True if there are duplicate values, False otherwise.
        """
        # Since the array is sorted, we can just check if adjacent elements are equal.
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return True
        return False


# Time Complexity: O(N), where N is the length of the input array. We iterate through the array once.
# Space Complexity: O(1), we use constant extra space.


# Test cases
solution = Solution()

print(solution.containsDuplicate([1, 2, 3, 4, 5]))  # Output: False
print(solution.containsDuplicate([1, 1, 2, 3, 4]))  # Output: True
print(solution.containsDuplicate([-1, 0, 0, 1, 2]))  # Output: True
print(solution.containsDuplicate([]))  # Output: False (empty array has no duplicates)
print(solution.containsDuplicate([1])) # Output: False (single element array has no duplicates)
```