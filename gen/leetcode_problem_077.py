```python
'''
# Alternating Sum
# Difficulty: Easy

# Problem Description:
# Given a non-empty list of integers nums, return the alternating sum. The alternating sum is calculated by subtracting an element at an even index from an element at an odd index, starting from the beginning of the list. If the list contains only one element, return that element.

# Examples:
# Example 1:
# Input: nums = [1, 2, 3, 4, 5]
# Output: -2
# Explanation: (1 - 2) + (3 - 4) + 5 = -2

# Example 2:
# Input: nums = [10]
# Output: 10
# Explanation: The list has only one element, so return that element.

# Example 3:
# Input: nums = [2, 4, 6, 8]
# Output: -8
# Explanation: (2-4) + (6-8) = -8

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
        n = len(nums)
        if n == 1:
            return nums[0]

        alt_sum = 0
        for i in range(0, n - 1, 2):
            alt_sum += nums[i] - nums[i+1]
        
        if n % 2 != 0:  # Handle the case where the length is odd
            alt_sum += nums[-1]
            
        return alt_sum
        


# Time Complexity: O(n), where n is the length of the input list nums.
# Space Complexity: O(1),  as we use only a few extra variables regardless of the input size.



# Test Cases
solution = Solution()

# Test Case 1
nums1 = [1, 2, 3, 4, 5]
print(f"Test Case 1: Input: {nums1}, Output: {solution.alternatingSum(nums1)}, Expected: -2")  # Output: -2

# Test Case 2
nums2 = [10]
print(f"Test Case 2: Input: {nums2}, Output: {solution.alternatingSum(nums2)}, Expected: 10")  # Output: 10

# Test Case 3
nums3 = [2, 4, 6, 8]
print(f"Test Case 3: Input: {nums3}, Output: {solution.alternatingSum(nums3)}, Expected: -8")  # Output: -8

# Test Case 4
nums4 = [1, 2, 3]
print(f"Test Case 4: Input: {nums4}, Output: {solution.alternatingSum(nums4)}, Expected: 2") # Output: 2


# Test Case 5 (Edge case: empty list -  although the constraints state the list is non-empty, it's good to handle this)
nums5 = []
print(f"Test Case 5: Input: {nums5}, Output: {solution.alternatingSum(nums5)}, Expected: 0") # Depending on how you want to handle it - you might raise an exception here instead. If you return 0, update the docstring to reflect that.


```