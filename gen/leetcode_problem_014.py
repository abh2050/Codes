```python
'''
# Alternating Sum
# Difficulty: Easy

# Problem Description:
# Given a non-empty list of integers nums, return the alternating sum. 
# The alternating sum is calculated by subtracting an element at an even index from the element at the previous odd index.
# If there are an odd number of elements, the last element is simply added to the sum.

# Examples:
# Example 1:
# Input: nums = [1, 2, 3, 4, 5]
# Output: -2
# Explanation: (1 - 2) + (3 - 4) + 5 = -2

# Example 2:
# Input: nums = [1, 2, 3, 4]
# Output: -2
# Explanation: (1 - 2) + (3 - 4) = -2

# Example 3:
# Input: nums = [1]
# Output: 1
# Explanation: 1

# Constraints:
# 1 <= nums.length <= 100
# -100 <= nums[i] <= 100
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
        n = len(nums)
        alt_sum = 0
        for i in range(0, n, 2):
            if i + 1 < n:
                alt_sum += nums[i] - nums[i + 1]
            else:  # Handles the case of an odd number of elements
                alt_sum += nums[i]
        return alt_sum


# Time Complexity: O(N), where N is the length of nums, as we iterate through the list once.
# Space Complexity: O(1), as we only use constant extra space.



# Test cases
solution = Solution()

# Test case 1
nums1 = [1, 2, 3, 4, 5]
print(f"Input: {nums1}, Output: {solution.alternatingSum(nums1)}")  # Expected Output: -2

# Test case 2
nums2 = [1, 2, 3, 4]
print(f"Input: {nums2}, Output: {solution.alternatingSum(nums2)}")  # Expected Output: -2

# Test case 3
nums3 = [1]
print(f"Input: {nums3}, Output: {solution.alternatingSum(nums3)}")  # Expected Output: 1

# Test case 4
nums4 = [10, 5, 20, 15]
print(f"Input: {nums4}, Output: {solution.alternatingSum(nums4)}")  # Expected Output: 0


# Test case 5 (Empty list - edge case, though constraint says list is non-empty)
nums5 = []
print(f"Input: {nums5}, Output: {solution.alternatingSum(nums5)}")  # Expected Output: 0


# Test case 6 (All negative numbers)
nums6 = [-1, -2, -3, -4, -5]
print(f"Input: {nums6}, Output: {solution.alternatingSum(nums6)}")  # Expected Output: -2

```