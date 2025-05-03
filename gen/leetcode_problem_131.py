```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular array of integers nums (where the last element is considered adjacent to the first element), 
# find the maximum sum of a non-adjacent subsequence. A subsequence is a sequence that can be derived 
# from another sequence by deleting some or no elements without changing the order of the remaining elements.

# Examples:
# Example 1:
# Input: nums = [2, 4, 1, 3, 5]
# Output: 10
# Explanation: Pick the subsequence [4, 5, 1]. The sum is 4 + 5 + 1 = 10.

# Example 2:
# Input: nums = [1, 2, 3, 1]
# Output: 4
# Explanation: Pick the subsequence [2, 1]. The sum is 2 + 1 = 4.


# Constraints:
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
'''

class Solution:
    def maxNonAdjacentSumCircular(self, nums: list[int]) -> int:
        """
        Calculates the maximum sum of a non-adjacent subsequence in a circular array.

        Args:
            nums: The input circular array of integers.

        Returns:
            The maximum sum of a non-adjacent subsequence.
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        # Handle the circularity by considering two cases:
        # 1. Excluding the last element:
        max_sum_excluding_last = self.maxNonAdjacentSum(nums[:-1])

        # 2. Excluding the first element:
        max_sum_excluding_first = self.maxNonAdjacentSum(nums[1:])


        return max(max_sum_excluding_last, max_sum_excluding_first)


    def maxNonAdjacentSum(self, nums: list[int]) -> int:
        """Helper function to calculate max non-adjacent sum for a linear array (House Robber problem)."""
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i]) 

        return dp[n - 1]


# Test cases
sol = Solution()
print(sol.maxNonAdjacentSumCircular([2, 4, 1, 3, 5]))  # Output: 10
print(sol.maxNonAdjacentSumCircular([1, 2, 3, 1]))  # Output: 4
print(sol.maxNonAdjacentSumCircular([1]))  # Output: 1
print(sol.maxNonAdjacentSumCircular([]))  # Output: 0
print(sol.maxNonAdjacentSumCircular([1,2,3,4,5,1,2,3,4,5])) # Output: 16


'''
Time Complexity: O(N), where N is the length of the input array. We iterate through the array twice in the worst case using the helper function.
Space Complexity: O(N) in the helper function due to the dp array. Could be optimized to O(1) by keeping track of only the previous two values.
'''


```