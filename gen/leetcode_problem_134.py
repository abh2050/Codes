```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular integer array nums, return the maximum possible sum of a non-empty subarray of nums, where no two elements in the subarray are adjacent.
# Consider the array circular, meaning the last element is considered adjacent to the first element.

# Examples:
# Example 1:
# Input: nums = [2,1,1,2]
# Output: 3
# Explanation: You can take nums[0] and nums[2] for a sum of 3.

# Example 2:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: You can take nums[0] and nums[2] for a sum of 4.

# Example 3:
# Input: nums = [1,1,1,1]
# Output: 2


# Constraints:
# 1 <= nums.length <= 3 * 10^4
# -100 <= nums[i] <= 100
'''

class Solution:
    def rob(self, nums: list[int]) -> int:
        """
        Calculates the maximum sum of non-adjacent elements in a circular array.

        Args:
            nums: The input circular integer array.

        Returns:
            The maximum possible sum.
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)

        # Consider two cases:
        # 1. Include the first element, exclude the last
        # 2. Exclude the first element, include the last
        def house_robber(arr):
            prev_max, curr_max = 0, 0
            for num in arr:
                temp = curr_max
                curr_max = max(curr_max, prev_max + num)
                prev_max = temp
            return curr_max

        return max(house_robber(nums[:-1]), house_robber(nums[1:]))

# Time Complexity: O(n) - We iterate through the array twice in house_robber.
# Space Complexity: O(1) - Constant extra space is used.


# Test Cases
solution = Solution()
print(solution.rob([2, 1, 1, 2]))  # Output: 3
print(solution.rob([1, 2, 3, 1]))  # Output: 4
print(solution.rob([1, 1, 1, 1]))  # Output: 2
print(solution.rob([1])) # Output 1
print(solution.rob([])) # Output 0
print(solution.rob([1,5])) # Output 5
print(solution.rob([1,3,1,3,100])) # output 103



```