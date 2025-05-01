```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular integer array nums (i.e., the last element is also adjacent to the first element), 
# find the maximum sum of a non-adjacent subsequence.  A subsequence is a sequence that can be derived 
# from another sequence by deleting some or no elements without changing the order of the remaining elements. 
# Non-adjacent means no two elements in the subsequence are adjacent in the original circular array.

# Examples:
# Example 1:
# Input: nums = [2,1,4,9]
# Output: 11
# Explanation: Choosing 2 and 9 yields a sum of 11, which is the maximum possible sum.

# Example 2:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Choosing 1 and 3 or 2 and 1 yields a maximum sum of 4.

# Example 3:
# Input: nums = [1]
# Output: 1

# Constraints:
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^4
'''

class Solution:
    def rob(self, nums: list[int]) -> int:
        """
        Calculates the maximum sum of non-adjacent elements in a circular array.

        Uses dynamic programming to efficiently find the maximum sum.  Handles the circularity
        by considering two cases: including the first element and excluding the first element.
        Then takes the maximum of the two results.

        Time complexity: O(n) - linear traversal of the array
        Space complexity: O(1) - constant extra space
        """
        n = len(nums)
        if n == 1:
            return nums[0]

        def rob_linear(arr):
            prev_prev = 0
            prev = 0
            for num in arr:
                curr = max(prev, prev_prev + num)
                prev_prev = prev
                prev = curr
            return prev

        # Case 1: Exclude the last element (equivalent to the first element in the circular array)
        max1 = rob_linear(nums[:-1])
        # Case 2: Exclude the first element
        max2 = rob_linear(nums[1:])

        return max(max1, max2)


# Test cases
solution = Solution()

# Test case 1
nums1 = [2, 1, 4, 9]
print(f"Test case 1: {solution.rob(nums1)}")  # Output: 11

# Test case 2
nums2 = [1, 2, 3, 1]
print(f"Test case 2: {solution.rob(nums2)}")  # Output: 4

# Test case 3
nums3 = [1]
print(f"Test case 3: {solution.rob(nums3)}")  # Output: 1

# Test case 4 (Edge case - all elements are the same)
nums4 = [5,5,5,5,5]
print(f"Test case 4: {solution.rob(nums4)}") # Output 10

# Test case 5 (larger array)
nums5 = [1,3,1,3,100]
print(f"Test case 5: {solution.rob(nums5)}") # Output 103


```