```python
'''
# Alternating Sum
# Difficulty: Easy

# Problem Description:
# Given a non-empty list of integers, return the alternating sum. The alternating sum is calculated by subtracting an element from the previous element, starting with the first element.

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
# 0 <= nums[i] <= 1000
'''

class Solution:
    def alternatingSum(self, nums: list[int]) -> int:
        """
        Calculates the alternating sum of a list of integers.

        Args:
            nums: A list of integers.

        Returns:
            The alternating sum.
        """
        alternating_sum = 0
        sign = 1  # Start with addition
        for num in nums:
            alternating_sum += sign * num
            sign *= -1  # Flip the sign for the next element
        return alternating_sum


# Time Complexity: O(n), where n is the length of the input list. We iterate through the list once.
# Space Complexity: O(1), we use constant extra space.


# Test Cases
solution = Solution()

# Example 1
nums1 = [1, 2, 3, 4, 5]
print(f"Input: {nums1}, Output: {solution.alternatingSum(nums1)}")  # Expected Output: 3

# Example 2
nums2 = [10, 5, 2]
print(f"Input: {nums2}, Output: {solution.alternatingSum(nums2)}")  # Expected Output: 7

# Example 3 - Single element list
nums3 = [7]
print(f"Input: {nums3}, Output: {solution.alternatingSum(nums3)}")  # Expected Output: 7

# Example 4 - Even length list
nums4 = [2, 4, 6, 8]
print(f"Input: {nums4}, Output: {solution.alternatingSum(nums4)}")  # Expected Output: -4

# Example 5 - Empty List (added to address a potential edge case, though not explicitly in the constraints)
nums5 = []
print(f"Input: {nums5}, Output: {solution.alternatingSum(nums5)}") # Expected Output: 0

```