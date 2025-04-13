```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular integer array nums, return the maximum possible sum of a non-empty subarray of nums,
# where no two elements in the subarray are adjacent.  "Circular" means the array connects end-to-end.

# Examples:
# Example 1:
# Input: nums = [2,4,8,9,2]
# Output: 13
# Explanation: The optimal subarray is [2, 8, 2], yielding a sum of 13.

# Example 2:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: The optimal subarray is [1,3], yielding a sum of 4.

# Constraints:
# 1 <= nums.length <= 3 * 10^4
# -3 * 10^4 <= nums[i] <= 3 * 10^4
'''

class Solution:
    def rob(self, nums: list[int]) -> int:
        """
        Calculates the maximum sum of non-adjacent elements in a circular array.

        This solution uses dynamic programming to calculate the maximum sum for two cases:
        1. Excluding the last element (like a regular non-circular array).
        2. Excluding the first element.
        The maximum of these two cases represents the optimal solution for the circular array.

        Time Complexity: O(n) - We iterate through the array twice.
        Space Complexity: O(1) - We use constant extra space.
        """
        n = len(nums)
        if n == 0: return 0  # Empty array case
        if n == 1: return nums[0] # Single element case

        def rob_linear(arr): # Helper function for linear array max sum
            prev, curr = 0, 0
            for num in arr:
                prev, curr = curr, max(curr, prev + num)
            return curr

        # Two cases: include first element or include last element (cannot include both)
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:])) if n>1 else nums[0]



# Test Cases
solution = Solution()

# Test case 1
nums1 = [2, 4, 8, 9, 2]
print(f"Input: {nums1}, Output: {solution.rob(nums1)} (Expected: 13)")

# Test case 2
nums2 = [1, 2, 3, 1]
print(f"Input: {nums2}, Output: {solution.rob(nums2)} (Expected: 4)")

# Test case 3: Edge case - single element
nums3 = [5]
print(f"Input: {nums3}, Output: {solution.rob(nums3)} (Expected: 5)")

# Test case 4: Edge case - empty array
nums4 = []
print(f"Input: {nums4}, Output: {solution.rob(nums4)} (Expected: 0)")

# Test case 5: All negative numbers
nums5 = [-2, -4, -1, -3]
print(f"Input: {nums5}, Output: {solution.rob(nums5)} (Expected: -1)")


# Test case 6: Mixed positive and negative numbers
nums6 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f"Input: {nums6}, Output: {solution.rob(nums6)} (Expected: 6)")

```