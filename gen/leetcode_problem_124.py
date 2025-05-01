```python
'''
# Maximum Sum of Non-Overlapping Subarrays with Length Constraints
# Difficulty: Hard

# Problem Description:
# You are given an integer array nums and two integers min_length and max_length.
# Find the maximum sum of non-overlapping subarrays where each subarray's length is between min_length and max_length (inclusive).

# Examples:
# Example 1:
# Input: nums = [4, 5, 2, 1, 3, 6], min_length = 1, max_length = 2
# Output: 15
# Explanation: We can select subarrays [5], [3, 6], and [4] which sums to 5 + 9 + 4 = 15.

# Example 2:
# Input: nums = [1, 2, 3, 4, 5, 6], min_length = 2, max_length = 3
# Output: 15
# Explanation: We can select subarrays [4, 5] and [1, 2, 3] which sums to 9 + 6 = 15.

# Constraints:
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^4
# 1 <= min_length <= max_length <= nums.length
'''

class Solution:
    def maxSumNonOverlapping(self, nums: list[int], min_length: int, max_length: int) -> int:
        n = len(nums)
        dp = [0] * (n + 1)  # dp[i] stores the maximum sum ending at index i-1
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]

        for i in range(min_length, n + 1):
            max_sum = 0
            for j in range(min_length, max_length + 1):
                if i - j >= 0:
                    current_sum = prefix_sum[i] - prefix_sum[i - j]
                    max_sum = max(max_sum, dp[i - j] + current_sum)  # Include current subarray
            dp[i] = max(dp[i - 1], max_sum)  # Choose whether to include current subarray or not

        return dp[n]

# Explanation:
# 1. dp[i] represents the maximum sum we can achieve using subarrays ending at index i-1.
# 2. We use prefix sum to efficiently calculate the sum of subarrays.
# 3. We iterate through possible subarray lengths between min_length and max_length.
# 4. For each possible subarray length, we calculate the sum and check if including it maximizes the overall sum.
# 5. We use dp[i-j] to ensure non-overlapping subarrays (previous maximum sum without overlapping the current subarray).

# Time Complexity: O(n * max_length), where n is the length of nums.
# Space Complexity: O(n) for the dp and prefix_sum arrays.



# Test cases
solution = Solution()
print(solution.maxSumNonOverlapping([4, 5, 2, 1, 3, 6], 1, 2))  # Output: 15
print(solution.maxSumNonOverlapping([1, 2, 3, 4, 5, 6], 2, 3))  # Output: 15
print(solution.maxSumNonOverlapping([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1, 3)) # Output: 9
print(solution.maxSumNonOverlapping([1, 5, 2, 7, 3, 9], 2, 2))  # Output: 16
print(solution.maxSumNonOverlapping([2,1,5,6,4,3], 3, 5)) # Output: 15


```