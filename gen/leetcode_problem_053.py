```python
'''
# Maximum Subsequence Sum with Non-Adjacent Differences Bounded

# Difficulty: Hard

# Problem Description:
# You are given an integer array nums and an integer k. You want to find the maximum possible sum of a non-empty subsequence of nums such that the absolute difference between any two adjacent elements in the subsequence is less than or equal to k.

# Examples:
# Example 1:
# Input: nums = [1, 5, 2, 7, 3], k = 2
# Output: 11
# Explanation: The optimal subsequence is [1, 2, 3, 5]. The sum is 11, and the differences between adjacent elements are |2 - 1| = 1, |3 - 2| = 1, and |5 - 3| = 2, all of which are less than or equal to k = 2.

# Example 2:
# Input: nums = [10, 2, 5, 1, 8, 20], k = 4
# Output: 35
# Explanation: The optimal subsequence is [2, 5, 8, 20]. The sum is 35, and the differences between adjacent elements are |5 - 2| = 3, |8 - 5| = 3, and |20 - 8| = 12.  However, note the elements are not necessarily adjacent in the original array.

# Constraints:
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 10^9
# 0 <= k <= 10^9
'''

class Solution:
    def maxSubsequenceSum(self, nums: list[int], k: int) -> int:
        # Sort the numbers to process them in ascending order.
        nums.sort()
        n = len(nums)

        # dp[i] stores the maximum subsequence sum ending with nums[i].
        dp = [0] * n
        dp[0] = nums[0]

        # Iterate through the sorted numbers.
        for i in range(1, n):
            dp[i] = nums[i] # Initialize with the current number.
            # For each previous number, check if the difference is within k.
            for j in range(i):
                if abs(nums[i] - nums[j]) <= k:
                    dp[i] = max(dp[i], dp[j] + nums[i])

        # Return the maximum value in dp.
        return max(dp)


# Time Complexity: O(n^2) due to the nested loops.
# Space Complexity: O(n) for the dp array.



# Test Cases
solution = Solution()

# Example 1
nums1 = [1, 5, 2, 7, 3]
k1 = 2
print(f"Example 1: {solution.maxSubsequenceSum(nums1, k1)}")  # Output: 11

# Example 2
nums2 = [10, 2, 5, 1, 8, 20]
k2 = 4
print(f"Example 2: {solution.maxSubsequenceSum(nums2, k2)}")  # Output: 35

# Example 3 - Edge case with k=0
nums3 = [1, 3, 5, 7, 9]
k3 = 0
print(f"Example 3: {solution.maxSubsequenceSum(nums3, k3)}") # Output: 9

# Example 4 - Edge case with all same elements
nums4 = [5, 5, 5, 5, 5]
k4 = 10
print(f"Example 4: {solution.maxSubsequenceSum(nums4, k4)}")  # Output: 25

# Example 5 - Large input
nums5 = list(range(1000))
k5 = 1000
print(f"Example 5: {solution.maxSubsequenceSum(nums5, k5)}") # Output: 499500

```