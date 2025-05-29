```python
'''
# Largest Element in an Array with its Index
# Difficulty: Easy

# Problem Description:
# Given an array of integers nums, find the largest element in the array and return it along with its index.
# If there are multiple largest elements, return the one with the smallest index.

# Examples:
# Example 1:
# Input: nums = [1, 5, 2, 8, 3]
# Output: [8, 3]
# Explanation: 8 is the largest element, and its index is 3.

# Example 2:
# Input: nums = [4, 2, 9, 9, 7]
# Output: [9, 2]
# Explanation: 9 is the largest element, and since there are two 9s, we return the one with the smaller index (2).

# Constraints:
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
'''

class Solution:
    def findLargestElement(self, nums: list[int]) -> list[int]:
        """
        Finds the largest element in an array and returns it with its index.

        Args:
            nums: The input array of integers.

        Returns:
            A list containing the largest element and its index.
        """
        # Initialize the largest element and its index
        largest_element = -float('inf')  # Initialize with negative infinity to handle negative numbers
        largest_index = -1

        # Iterate through the array
        for i, num in enumerate(nums):
            # If the current element is greater than the current largest, update the largest element and its index
            if num > largest_element:
                largest_element = num
                largest_index = i

        return [largest_element, largest_index]


'''
# Time Complexity: O(n), as we iterate through the array once.
# Space Complexity: O(1), as we only use constant extra space.
'''

# Test cases
solution = Solution()

nums1 = [1, 5, 2, 8, 3]
print(solution.findLargestElement(nums1))  # Output: [8, 3]

nums2 = [4, 2, 9, 9, 7]
print(solution.findLargestElement(nums2))  # Output: [9, 2]

nums3 = [-5, -2, -1, -8, -3]
print(solution.findLargestElement(nums3))  # Output: [-1, 2]

nums4 = [1]
print(solution.findLargestElement(nums4))  # Output: [1, 0]

nums5 = []
print(solution.findLargestElement(nums5)) # Output: [-inf, -1] 
# The empty array case returns the initial values as there are no elements to check against


```
