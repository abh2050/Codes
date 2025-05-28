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
        Counts the number of elements in the input list with an even number of digits.

        Args:
            nums: A list of integers.

        Returns:
            The count of numbers with an even number of digits.
        """

        count = 0
        for num in nums:
            # Convert number to string to easily get the number of digits
            num_str = str(num)
            if len(num_str) % 2 == 0:
                count += 1
        return count


# Test Cases
solution = Solution()

# Example 1
nums1 = [12, 345, 2, 6, 7896]
output1 = solution.findNumbers(nums1)  # Expected output: 2
print(f"Test Case 1: Input = {nums1}, Output = {output1}")
assert output1 == 2


# Example 2
nums2 = [555, 901, 482, 1771]
output2 = solution.findNumbers(nums2)  # Expected output: 1
print(f"Test Case 2: Input = {nums2}, Output = {output2}")
assert output2 == 1


# Example 3 - Edge Case: Empty list
nums3 = []
output3 = solution.findNumbers(nums3)  # Expected output: 0
print(f"Test Case 3: Input = {nums3}, Output = {output3}")
assert output3 == 0



# Example 4 - Edge case: single-digit numbers
nums4 = [1, 2, 3, 4, 5]
output4 = solution.findNumbers(nums4)  # Expected output: 0
print(f"Test Case 4: Input = {nums4}, Output = {output4}")
assert output4 == 0


# Time and Space Complexity Analysis:
# Time Complexity: O(n*m) where n is the length of nums and m is the max number of digits in any num in nums because str(num) takes O(m) time to convert an integer to string.
# Space Complexity: O(m)  String conversion creates a string of length m in the worst case. However, if we consider only auxiliary space complexity (excluding the input), it's O(1) because we aren't using any extra space that scales with the input size.


```