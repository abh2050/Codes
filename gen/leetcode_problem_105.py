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
            # Convert number to string to easily get digit count
            num_str = str(num)
            if len(num_str) % 2 == 0:
                count += 1
        return count
        


# Time Complexity: O(N*M) where N is the length of nums and M is the max number of digits of any number.
# In the worst case scenario, all numbers have the same length, so we iterate over all the digits.
# However, since the constraint states the max number is 10^5 (max 6 digits), M can be considered a constant, so O(N).

# Space Complexity: O(1) as we're not using any extra space that scales with input size.
# The space used for num_str is constant regardless of the input size as well due to the constraint of max 10^5


# Test cases
solution = Solution()

print(solution.findNumbers([12, 345, 2, 6, 7896]))  # Output: 2
print(solution.findNumbers([555, 901, 482, 1771]))  # Output: 1
print(solution.findNumbers([1,2,3,4,5,6,7,8,9,100000])) # Output: 1
print(solution.findNumbers([])) # Output: 0
print(solution.findNumbers([100000])) #Output 1





```