```python
'''
# Check for Even Digits
# Difficulty: Easy

# Problem Description:
# Given an integer array nums, return the number of elements in nums that have an even number of digits.

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
        Counts the number of elements in nums with an even number of digits.

        Args:
            nums: A list of integers.

        Returns:
            The count of numbers with an even number of digits.
        """

        count = 0
        for num in nums:
            # Convert number to string and check its length
            if len(str(num)) % 2 == 0:
                count += 1
        return count


# Time Complexity: O(N*log10(M)), where N is the length of the input array and M is the maximum value in the array.
#  Converting a number to a string takes logarithmic time with respect to the number itself (base 10).

# Space Complexity: O(1). We only use a few extra variables for counting and iterations, 
# which doesn't scale with the input size.


# Test Cases
solution = Solution()

# Test Case 1
nums1 = [12, 345, 2, 6, 7896]
output1 = solution.findNumbers(nums1)
print(f"Test Case 1: Input: {nums1}, Output: {output1}, Expected: 2")  # Expected: 2

# Test Case 2
nums2 = [555, 901, 482, 1771]
output2 = solution.findNumbers(nums2)
print(f"Test Case 2: Input: {nums2}, Output: {output2}, Expected: 1")  # Expected: 1

# Test Case 3 (Empty array)
nums3 = []
output3 = solution.findNumbers(nums3)
print(f"Test Case 3: Input: {nums3}, Output: {output3}, Expected: 0") # Expected 0

# Test Case 4 (Large Number)
nums4 = [100000]
output4 = solution.findNumbers(nums4)
print(f"Test Case 4: Input: {nums4}, Output: {output4}, Expected: 1") # Expected 1



```