```python
'''
# Alternating Sum

# Difficulty: Easy

# Problem Description:
# Given a non-empty list of integers, return the alternating sum.  
# The alternating sum is calculated by subtracting each even-indexed element 
# from the sum of odd-indexed elements.

# Examples:
# Example 1:
# Input: nums = [1, 2, 3, 4, 5]
# Output: 3
# Explanation: (1 + 3 + 5) - (2 + 4) = 9 - 6 = 3

# Example 2:
# Input: nums = [10, 20, 30]
# Output: -20
# Explanation: (10 + 30) - 20 = 40 - 20 = 20

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
        odd_sum = 0
        even_sum = 0

        for i in range(len(nums)):
            if i % 2 == 0:  # Odd-indexed (0-based indexing)
                odd_sum += nums[i]
            else:  # Even-indexed
                even_sum += nums[i]

        return odd_sum - even_sum
    
    '''
    Time Complexity: O(n), where n is the length of the input list `nums`. We iterate through the list once.
    Space Complexity: O(1), as we only use a few variables to store sums, which is constant space.
    '''


# Test cases
solution = Solution()

# Example 1
nums1 = [1, 2, 3, 4, 5]
print(f"Input: {nums1}, Output: {solution.alternatingSum(nums1)}")  # Expected output: 3

# Example 2
nums2 = [10, 20, 30]
print(f"Input: {nums2}, Output: {solution.alternatingSum(nums2)}")  # Expected output: 20

# Example 3 - Empty list
nums3 = []
print(f"Input: {nums3}, Output: {solution.alternatingSum(nums3)}")  # Expected output: 0

# Example 4 - Single element
nums4 = [7]
print(f"Input: {nums4}, Output: {solution.alternatingSum(nums4)}")  # Expected output: 7

# Example 5 - All even numbers
nums5 = [2,4,6,8]
print(f"Input: {nums5}, Output: {solution.alternatingSum(nums5)}") # Expected Output: -6

# Example 6 - All odd numbers
nums6 = [1, 3, 5, 7]
print(f"Input: {nums6}, Output: {solution.alternatingSum(nums6)}")  # Expected Output: 16



```