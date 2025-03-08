```python
'''
# Alternating Sum

# Difficulty: Easy

# Problem Description:
# Given a non-empty list of integers nums, return the alternating sum. 
# The alternating sum is calculated by subtracting each odd-indexed element 
# from the sum of even-indexed elements.  Indexing starts at 0.

# Examples:
# Example 1:
# Input: nums = [1, 2, 3, 4, 5]
# Output: 3
# Explanation: (1 + 3 + 5) - (2 + 4) = 9 - 6 = 3

# Example 2:
# Input: nums = [10, 20, 30]
# Output: -10
# Explanation: (10 + 30) - (20) = 40 - 20 = 20

# Constraints:
# 1 <= len(nums) <= 100
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
        even_sum = 0
        odd_sum = 0
        for i, num in enumerate(nums):
            if i % 2 == 0:
                even_sum += num
            else:
                odd_sum += num
        return even_sum - odd_sum

        # Alternative one-liner using list comprehensions and sum()
        # return sum(nums[::2]) - sum(nums[1::2])


# Time Complexity: O(n), where n is the length of the input list nums. We iterate through the list once.
# Space Complexity: O(1), as we only use a few variables to store sums, independent of the input size.


# Test Cases
solution = Solution()

# Test Case 1
nums1 = [1, 2, 3, 4, 5]
print(f"Test Case 1: Input: {nums1}, Output: {solution.alternatingSum(nums1)}, Expected: 3")  # Output: 3

# Test Case 2
nums2 = [10, 20, 30]
print(f"Test Case 2: Input: {nums2}, Output: {solution.alternatingSum(nums2)}, Expected: 20") # Output: 20


# Test Case 3 (Edge case - single element)
nums3 = [7]
print(f"Test Case 3: Input: {nums3}, Output: {solution.alternatingSum(nums3)}, Expected: 7")  # Output: 7

# Test Case 4 (Edge case - empty list.  Though constraints say non-empty, good to test)
nums4 = []
print(f"Test Case 4: Input: {nums4}, Output: {solution.alternatingSum(nums4)}, Expected: 0")  # Output: 0
```