```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular integer array nums, return the maximum possible sum of a non-empty subarray of nums such that no two elements in the subarray are adjacent.
# In a circular array, the first and last elements are considered adjacent.

# Examples:
# Example 1:
# Input: nums = [2,1,2,7,3]
# Output: 10
# Explanation: You can choose the subarray [2,2,3] with a sum of 7 or the subarray [1,7] with a sum of 8, the maximum sum of non-adjacent element is [2,7,3], giving a sum of 10.

# Example 2:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: You can choose the subarray [1,3] with a sum of 4.

# Constraints:
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^4
'''

class Solution:
    def rob_circular(self, nums: list[int]) -> int:
        """
        Calculates the maximum sum of non-adjacent elements in a circular array.

        Uses dynamic programming to calculate the maximum sum for two cases:
        1. Excluding the last element (treating the array as linear)
        2. Excluding the first element (treating the array as linear)

        The maximum of these two cases is the result.

        Time Complexity: O(N) - We iterate through the array twice.
        Space Complexity: O(1) - We only use a few variables for storage.
        """
        n = len(nums)
        if n == 1:
            return nums[0]

        def rob_linear(arr):
            prev1, prev2 = 0, 0
            for num in arr:
                current = max(num + prev2, prev1)
                prev2 = prev1
                prev1 = current
            return prev1

        # Case 1: Exclude last element
        max1 = rob_linear(nums[:-1])
        # Case 2: Exclude first element
        max2 = rob_linear(nums[1:])

        return max(max1, max2)


# Test Cases
solution = Solution()

# Example 1
nums1 = [2, 1, 2, 7, 3]
print(f"Input: {nums1}, Output: {solution.rob_circular(nums1)}")  # Expected Output: 10

# Example 2
nums2 = [1, 2, 3, 1]
print(f"Input: {nums2}, Output: {solution.rob_circular(nums2)}")  # Expected Output: 4

# Example 3: Single element array
nums3 = [5]
print(f"Input: {nums3}, Output: {solution.rob_circular(nums3)}")  # Expected Output: 5

# Example 4: Two element array
nums4 = [1, 2]
print(f"Input: {nums4}, Output: {solution.rob_circular(nums4)}")  # Expected Output: 2

# Example 5: All equal elements
nums5 = [3, 3, 3, 3]
print(f"Input: {nums5}, Output: {solution.rob_circular(nums5)}")  # Expected Output: 6


```