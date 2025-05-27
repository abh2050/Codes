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
# Only 1771 contains an even number of digits.

# Constraints:
# 1 <= nums.length <= 500
# 1 <= nums[i] <= 10^5
'''

class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        """
        Counts the number of integers in a list with an even number of digits.

        Args:
            nums: A list of integers.

        Returns:
            The count of integers with an even number of digits.
        """
        count = 0
        for num in nums:
            if len(str(num)) % 2 == 0:  # Convert to string to find the number of digits
                count += 1
        return count

# Time Complexity: O(N*M) where N is the length of nums, and M is the average number of digits in each number. 
# Converting an integer to a string takes time proportional to the number of digits.

# Space Complexity: O(1).  We are not using any extra space that scales with the input size. The string conversion is temporary and doesn't contribute significantly to space complexity.


# Test Cases
solution = Solution()
print(solution.findNumbers([12, 345, 2, 6, 7896]))  # Output: 2
print(solution.findNumbers([555, 901, 482, 1771]))  # Output: 1
print(solution.findNumbers([1, 10, 100, 1000, 10000])) # Output: 2
print(solution.findNumbers([]))  # Output: 0 
print(solution.findNumbers([100000])) # Output: 0




```