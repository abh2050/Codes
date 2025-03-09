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
# Only 1771 contains an even number of digits.

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
            # Convert the number to a string to easily find the number of digits
            num_str = str(num)
            if len(num_str) % 2 == 0:
                count += 1
        return count
        
# Time Complexity: O(N*M) where N is the length of nums and M is the average number of digits in each number.  In the worst case, M is a constant (5 in this problem due to the constraint), so it simplifies to O(N).
# Space Complexity: O(1) as we're only using a few extra variables, independent of the input size.


# Test Cases
solution = Solution()

print(solution.findNumbers([12, 345, 2, 6, 7896]))  # Expected: 2
print(solution.findNumbers([555, 901, 482, 1771]))  # Expected: 1
print(solution.findNumbers([1]))  # Expected: 0
print(solution.findNumbers([100000])) # Expected: 1 # Testing the upper bound constraint
print(solution.findNumbers([]))  # Expected: 0 # Testing an empty list
```