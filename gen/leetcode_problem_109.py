```python
'''
# Check for Even Digits
# Difficulty: Easy

# Problem Description:
# Given an integer array nums, return the number of integers in nums that have an even number of digits.

# Examples:
# Example 1:
# Input: nums = [12,345,2,6,7896]
# Output: 2
# Explanation: 
# 12 contains 2 digits (even number of digits). 
# 345 contains 3 digits (odd number of digits). 
# 2 contains 1 digit (odd number of digits). 
# 6 contains 1 digit (odd number of digits). 
# 7896 contains 4 digits (even number of digits). 
# Therefore only 12 and 7896 contain an even number of digits.

# Example 2:
# Input: nums = [555,901,482,1771]
# Output: 1 
# Explanation: 
# Only 482 contains an even number of digits.

# Constraints:
# 1 <= nums.length <= 500
# 1 <= nums[i] <= 10^5
'''

class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        """
        Counts the number of integers in the input list with an even number of digits.

        Args:
            nums: A list of integers.

        Returns:
            The count of integers with an even number of digits.
        """

        count = 0
        for num in nums:
            # Convert the number to a string to easily find its length
            num_str = str(num)
            if len(num_str) % 2 == 0:
                count += 1
        return count

# Time Complexity: O(n*m) where n is the length of nums and m is the maximum number of digits in any number. In the worst-case, we iterate through all numbers in nums and convert each to a string, which takes time proportional to the number of digits. However, since the maximum number of digits is bounded (10^5 max, implying at most 6 digits), this can be considered O(n) for practical purposes.
# Space Complexity: O(1). We are not using any extra space that scales with the input size. The space used for the string conversion is constant as the largest number has a bounded number of digits.


# Test Cases
solution = Solution()

# Test Case 1
nums1 = [12, 345, 2, 6, 7896]
print(f"Test Case 1: Input: {nums1}, Output: {solution.findNumbers(nums1)}, Expected: 2")

# Test Case 2
nums2 = [555, 901, 482, 1771]
print(f"Test Case 2: Input: {nums2}, Output: {solution.findNumbers(nums2)}, Expected: 1")

# Test Case 3 - Empty list
nums3 = []
print(f"Test Case 3: Input: {nums3}, Output: {solution.findNumbers(nums3)}, Expected: 0")


# Test Case 4- Single digit numbers
nums4 = [1,2,3,4,5]
print(f"Test Case 4: Input: {nums4}, Output: {solution.findNumbers(nums4)}, Expected: 0")


# Test Case 5 - Larger numbers
nums5 = [123456, 1234, 12]
print(f"Test Case 5: Input: {nums5}, Output: {solution.findNumbers(nums5)}, Expected: 2")


```