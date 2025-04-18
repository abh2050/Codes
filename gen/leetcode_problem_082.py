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
# Explanation: The list is empty, so we return -1.


# Constraints:
# 0 <= len(nums) <= 10^4
# -10^5 <= nums[i] <= 10^5
# nums is sorted in ascending order (non-decreasing).
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


# Time Complexity: O(1) because we are accessing the last element directly using indexing, which takes constant time.
# Space Complexity: O(1) because we are not using any extra space.


# Test cases
solution = Solution()
print(solution.findLargest([1, 2, 3, 4, 5]))  # Output: 5
print(solution.findLargest([-5, -3, 0, 2]))  # Output: 2
print(solution.findLargest([]))  # Output: -1
print(solution.findLargest([-100, -50, 0, 50, 100])) # Output: 100
print(solution.findLargest([1])) # Output: 1


```