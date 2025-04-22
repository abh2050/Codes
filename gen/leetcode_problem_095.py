```python
'''
# Count Odd Numbers in an Array
# Difficulty: Easy

# Problem Description:
# Given an array of integers nums, return the count of odd numbers in the array.

# Examples:
# Example 1:
# Input: nums = [1, 2, 3, 4, 5]
# Output: 3
# Explanation: The odd numbers are 1, 3, and 5.

# Example 2:
# Input: nums = [2, 4, 6, 8]
# Output: 0
# Explanation: There are no odd numbers in the array.

# Example 3:
# Input: nums = []
# Output: 0
# Explanation: There are no numbers in the array.


# Constraints:
# 0 <= nums.length <= 5000
# -1000 <= nums[i] <= 1000
'''

class Solution:
    def countOdds(self, nums: list[int]) -> int:
        """
        Counts the number of odd integers in a given array.

        Args:
            nums: A list of integers.

        Returns:
            The number of odd integers in nums.
        """

        count = 0
        for num in nums:
            if num % 2 != 0:  # Check for odd numbers using the modulo operator
                count += 1
        return count

    # Time Complexity: O(n), where n is the length of the input array nums. 
    # We iterate through the array once.

    # Space Complexity: O(1). We only use a constant amount of extra space.



# Test cases
solution = Solution()

# Test case 1
nums1 = [1, 2, 3, 4, 5]
print(f"Test case 1: Input: {nums1}, Output: {solution.countOdds(nums1)}, Expected: 3")

# Test case 2
nums2 = [2, 4, 6, 8]
print(f"Test case 2: Input: {nums2}, Output: {solution.countOdds(nums2)}, Expected: 0")

# Test case 3
nums3 = []
print(f"Test case 3: Input: {nums3}, Output: {solution.countOdds(nums3)}, Expected: 0")

# Test case 4 (Larger array)
nums4 = list(range(1, 1001)) # Numbers 1 to 1000
print(f"Test case 4: Input: (Range 1-1000), Output: {solution.countOdds(nums4)}, Expected: 500")

# Test case 5 (Negative numbers)
nums5 = [-1, -2, -3, -4, -5]
print(f"Test case 5: Input: {nums5}, Output: {solution.countOdds(nums5)}, Expected: 3")


```