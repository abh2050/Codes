```python
'''
# Largest Element in a Sorted List
# Difficulty: Easy

# Problem Description:
# Given a sorted list of integers, find and return the largest element.
# If the list is empty, return -1.

# Examples:
# Example 1:
# Input: nums = [1, 2, 3, 4, 5]
# Output: 5
# Explanation: The largest element in the list is 5.

# Example 2:
# Input: nums = [-5, -3, 0, 2]
# Output: 2
# Explanation: The largest element in the list is 2.

# Example 3:
# Input: nums = []
# Output: -1
# Explanation: The list is empty.

# Constraints:
# 0 <= len(nums) <= 10^4
# -10^9 <= nums[i] <= 10^9
'''

class Solution:
    def findLargest(self, nums: list[int]) -> int:
        """
        Finds the largest element in a sorted list.

        Args:
            nums: A sorted list of integers.

        Returns:
            The largest element in the list, or -1 if the list is empty.
        """
        n = len(nums)
        if n == 0:
            return -1
        else:
            return nums[n - 1]  # Since the list is sorted, the last element is the largest


# Time Complexity: O(1) because we are directly accessing the last element.
# Space Complexity: O(1) because we are not using any extra space.


# Test cases
solution = Solution()

# Test case 1
nums1 = [1, 2, 3, 4, 5]
print(f"Test case 1: {solution.findLargest(nums1)}")  # Output: 5

# Test case 2
nums2 = [-5, -3, 0, 2]
print(f"Test case 2: {solution.findLargest(nums2)}")  # Output: 2

# Test case 3
nums3 = []
print(f"Test case 3: {solution.findLargest(nums3)}")  # Output: -1

# Test case 4 - large list
nums4 = list(range(10000))
print(f"Test case 4: {solution.findLargest(nums4)}") # Output: 9999

# Test case 5 - negative numbers
nums5 = [-5, -4, -3, -2]
print(f"Test case 5: {solution.findLargest(nums5)}") # Output: -2
```