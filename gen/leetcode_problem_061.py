```python
'''
# Alternating Sum
# Difficulty: Easy

# Problem Description:
# Given a non-empty list of integers nums, return the alternating sum of its elements.
# The alternating sum is calculated by subtracting the second element from the first,
# adding the third element to the result, subtracting the fourth element, and so on.

# Examples:
# Example 1:
# Input: nums = [1, 2, 3, 4, 5]
# Output: 3
# Explanation: 1 - 2 + 3 - 4 + 5 = 3

# Example 2:
# Input: nums = [10, 5, 2]
# Output: 7
# Explanation: 10 - 5 + 2 = 7

# Constraints:
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 1000
'''

class Solution:
    def alternatingSum(self, nums: list[int]) -> int:
        """
        Calculates the alternating sum of a list of integers.

        Args:
            nums: A list of integers.

        Returns:
            The alternating sum of the integers.
        """

        alternating_sum = 0
        for i, num in enumerate(nums):
            if i % 2 == 0:  # Even indices are added
                alternating_sum += num
            else:  # Odd indices are subtracted
                alternating_sum -= num
        return alternating_sum

# Time Complexity: O(n), where n is the length of the input list nums. We iterate through the list once.
# Space Complexity: O(1), as we only use a constant amount of extra space.


# Test Cases
solution = Solution()

# Test Case 1
nums1 = [1, 2, 3, 4, 5]
print(f"Input: {nums1}, Output: {solution.alternatingSum(nums1)}")  # Expected Output: 3

# Test Case 2
nums2 = [10, 5, 2]
print(f"Input: {nums2}, Output: {solution.alternatingSum(nums2)}")  # Expected Output: 7

# Test Case 3 (Empty List - Edge Case, added to demonstrate handling although constraint specifies non-empty)
nums3 = []  
print(f"Input: {nums3}, Output: {solution.alternatingSum(nums3)}")  # Expected Output: 0


# Test Case 4 (Single Element List)
nums4 = [7]
print(f"Input: {nums4}, Output: {solution.alternatingSum(nums4)}")  # Expected Output: 7

# Test Case 5 (Larger list)
nums5 = [100, 200, 300, 400, 500, 600]
print(f"Input: {nums5}, Output: {solution.alternatingSum(nums5)}") # Expected Output: -300
```