```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular array of integers nums, find the maximum possible sum you can get from a set of non-adjacent elements.
# In a circular array, the last element is considered adjacent to the first element.

# Examples:
# Example 1:
# Input: nums = [2, 7, 9, 3, 1]
# Output: 11
# Explanation: Pick nums[0], nums[2], and nums[4].

# Example 2:
# Input: nums = [1, 2, 3, 1]
# Output: 4
# Explanation: Pick nums[0] and nums[2].

# Constraints:
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^4
'''

class Solution:
    def rob(self, nums: list[int]) -> int:
        """
        Calculates the maximum sum of non-adjacent elements in a circular array.

        Args:
            nums: The input circular array of integers.

        Returns:
            The maximum possible sum of non-adjacent elements.
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)

        # Consider two scenarios:
        # 1. Include the first element: Then we can't include the last element.
        # 2. Exclude the first element: Then we can include the last element.
        # Return the maximum of these two scenarios.

        def house_robber(arr):  # Helper function for standard house robber problem (linear array)
            dp = [0] * len(arr)
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])
            for i in range(2, len(arr)):
                dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])
            return dp[-1]

        include_first = house_robber(nums[:-1])  # Exclude last element
        exclude_first = house_robber(nums[1:])  # Exclude first element

        return max(include_first, exclude_first)


# Test Cases
solution = Solution()

# Example 1
nums1 = [2, 7, 9, 3, 1]
print(f"Input: {nums1}, Output: {solution.rob(nums1)} (Expected: 11)")

# Example 2
nums2 = [1, 2, 3, 1]
print(f"Input: {nums2}, Output: {solution.rob(nums2)} (Expected: 4)")

# Example 3: Edge case - single element
nums3 = [5]
print(f"Input: {nums3}, Output: {solution.rob(nums3)} (Expected: 5)")

# Example 4: Edge case - two elements
nums4 = [1, 5]
print(f"Input: {nums4}, Output: {solution.rob(nums4)} (Expected: 5)")

# Example 5: All equal elements
nums5 = [3,3,3,3]
print(f"Input: {nums5}, Output: {solution.rob(nums5)} (Expected: 6)")


''' Time Complexity: O(n), as we iterate through the array twice in the house_robber function.
    Space Complexity: O(n) for the dp array in the house_robber function. Can be optimized to O(1) by using variables instead of array.'''

```