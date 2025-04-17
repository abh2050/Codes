```python
'''
# Alternating Sum
# Difficulty: Easy

# Problem Description:
# Given a non-empty list of integers nums, return the alternating sum. The alternating sum is calculated by subtracting an element at an even index from the element at the preceding odd index. In other words, it's nums[1] - nums[0] + nums[3] - nums[2] + ... . If the list has an odd number of elements, the last element is added to the sum.


# Examples:
# Example 1:
# Input: nums = [1, 2, 3, 4, 5]
# Output: 3
# Explanation: (2 - 1) + (4 - 3) + 5 = 1 + 1 + 5 = 3

# Example 2:
# Input: nums = [10, 20, 30, 40]
# Output: 20
# Explanation: (20 - 10) + (40 - 30) = 10 + 10 = 20

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
             The alternating sum.
        """
        n = len(nums)
        alt_sum = 0
        for i in range(0, n, 2):
            if i + 1 < n:
                alt_sum += nums[i + 1] - nums[i]
            else:
                alt_sum += nums[i]  # Add the last element if the list has odd length
        return alt_sum

# Time Complexity: O(n), as we iterate through the list once.
# Space Complexity: O(1), as we use constant extra space.



# Test Cases
solution = Solution()

# Example 1
nums1 = [1, 2, 3, 4, 5]
print(f"Input: {nums1}, Output: {solution.alternatingSum(nums1)}")  # Expected: 3

# Example 2
nums2 = [10, 20, 30, 40]
print(f"Input: {nums2}, Output: {solution.alternatingSum(nums2)}")  # Expected: 20

# Example 3 - Odd length
nums3 = [1, 2, 3]
print(f"Input: {nums3}, Output: {solution.alternatingSum(nums3)}")  # Expected: 2

# Example 4 - Single element
nums4 = [7]
print(f"Input: {nums4}, Output: {solution.alternatingSum(nums4)}")  # Expected: 7


# Example 5 - Empty List (Edge Case - should ideally be handled in constraints)
nums5 = []
print(f"Input: {nums5}, Output: {solution.alternatingSum(nums5)}")  # Expected: 0



```