```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular integer array nums, return the maximum possible sum of a non-empty subarray of nums, where non-adjacent elements are chosen.
# A circular array means the end of the array connects to the beginning of the array.  Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n], where n is the length of nums.
# A subarray may only include each element of the original array once.


# Examples:
# Example 1:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: You can take elements at index 0 and 2 to form a sum of 1 + 3 = 4.

# Example 2:
# Input: nums = [2,7,9,3,1]
# Output: 11
# Explanation: You can take elements at indices 0, 2, and 4 to form a sum of 2 + 9 + 1 = 11.

# Constraints:
# 1 <= nums.length <= 3 * 10^4
# -10^4 <= nums[i] <= 10^4
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
        if n == 1:
            return nums[0]
        
        # Handle the circularity by considering two cases:
        # 1. Include the first element, exclude the last
        # 2. Exclude the first element, include the last
        return max(self.house_robber(nums[:-1]), self.house_robber(nums[1:]))

    def house_robber(self, nums: list[int]) -> int:
        """
        Helper function to solve the standard house robber problem (non-circular).
        Uses dynamic programming to store maximum sums at each index.

        Args:
            nums: The input integer array.

        Returns:
            The maximum possible sum of non-adjacent elements.
        """

        n = len(nums)
        if not n:  # Handle empty input. Should not happen in main context, but good practice
            return 0
        if n == 1:
            return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[n - 1]


# Time Complexity: O(N), where N is the number of elements in the array. We traverse the array twice.
# Space Complexity: O(N) for the dp array in the house_robber helper function.


# Test cases
solution = Solution()
print(solution.rob([1, 2, 3, 1]))  # Output: 4
print(solution.rob([2, 7, 9, 3, 1]))  # Output: 11
print(solution.rob([1]))  # Output: 1
print(solution.rob([2,3,2])) # Output: 3
print(solution.rob([1,3,1,3,100])) # Output 103


```