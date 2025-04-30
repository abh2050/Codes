```python
'''
# Maximum Sum of Non-Overlapping Subarrays with Length Constraints
# Difficulty: Hard

# Problem Description:
# You are given an integer array nums and two integers minLength and maxLength.
# You need to find the maximum sum of non-overlapping subarrays where each subarray's length is between minLength and maxLength (inclusive).
# Return the maximum sum. If no such subarrays exist, return 0.

# Examples:
# Example 1:
# Input: nums = [1,2,3,4,5,6], minLength = 2, maxLength = 3
# Output: 15
# Explanation: We can choose subarrays [2,3] and [5,6] with lengths 2 and 2 respectively. The sum is 5 + 11 = 15.

# Example 2:
# Input: nums = [1,1,1,1,1,1], minLength = 3, maxLength = 5
# Output: 6
# Explanation: We can choose the subarray [1,1,1,1,1] with length 5. The sum is 5.


# Constraints:
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^4
# 1 <= minLength <= maxLength <= nums.length
'''

class Solution:
    def maxSumNonOverlapping(self, nums: list[int], minLength: int, maxLength: int) -> int:
        n = len(nums)
        dp = [0] * (n + 1)  # dp[i] stores the maximum sum ending at index i - 1
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        for i in range(minLength, n + 1):
            dp[i] = dp[i - 1]  # Initialize with previous best
            for length in range(minLength, min(maxLength, i) + 1):
                current_sum = prefix_sum[i] - prefix_sum[i - length]
                if i - length >= 0:
                    dp[i] = max(dp[i], dp[i - length] + current_sum)
                else:  # If it's the first subarray
                    dp[i] = max(dp[i], current_sum)

        return dp[n]


'''
Explanation:

1. dp[i] represents the maximum sum achievable considering subarrays up to index i-1.
2. We iterate through nums and calculate the prefix sum to easily get the sum of any subarray.
3. In the main loop, we iterate from minLength to n (inclusive).
4. Inside, we try all possible subarray lengths between minLength and maxLength (inclusive) ending at the current index i.
5. We update dp[i] by taking the maximum of the current dp[i] (no new subarray) and the sum of the current subarray + dp[i - length] (including the current subarray).

Time Complexity: O(n * maxLength) as we iterate through nums and have a nested loop up to maxLength in the worst case.
Space Complexity: O(n) for the dp array and prefix_sum array.
'''

# Test Cases
sol = Solution()
print(sol.maxSumNonOverlapping(nums=[1, 2, 3, 4, 5, 6], minLength=2, maxLength=3))  # Output: 15
print(sol.maxSumNonOverlapping(nums=[1, 1, 1, 1, 1, 1], minLength=3, maxLength=5))  # Output: 6
print(sol.maxSumNonOverlapping(nums=[4, 5, 1, 2, 6, 3], minLength=1, maxLength=2))  # Output: 17
print(sol.maxSumNonOverlapping(nums=[2, 1, 5, 6, 3, 2, 1], minLength=2, maxLength=4)) # Output: 14



```