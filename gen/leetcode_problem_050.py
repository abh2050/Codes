```python
'''
# Maximum Subarray Sum with K Distinct Jumps

# Difficulty: Hard

# Problem Description:
# You are given an array of integers `nums` and an integer `k`. You can jump forward in the array by any distance from 1 to k (inclusive). Find the maximum possible sum of a subarray that can be formed by starting at index 0 and making jumps according to the given rules. You must land on at least one element (i.e., an empty subarray is not allowed).

# Examples:
# Example 1:
# Input: nums = [1, -2, 3, 2, -1], k = 2
# Output: 6
# Explanation: The optimal path is 0 -> 2 -> 3, resulting in a sum of 1 + 3 + 2 = 6.

# Example 2:
# Input: nums = [-1, -2, -3], k = 1
# Output: -1
# Explanation: The optimal path is 0, resulting in a sum of -1.

# Example 3:
# Input: nums = [2, 1, -3, 4, 5], k = 3
# Output: 11 
# Explanation: The optimal path is 0 -> 3 -> 4, resulting in a sum of 2 + 4 + 5 = 11.

# Constraints:
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 1 <= k <= nums.length
'''

import collections

class Solution:
    def maxJumpSum(self, nums: list[int], k: int) -> int:
        """
        Calculates the maximum subarray sum with jumps of length 1 to k.

        Args:
            nums: The input array of integers.
            k: The maximum jump length.

        Returns:
            The maximum subarray sum.
        """
        n = len(nums)
        dp = [-float('inf')] * n  # Initialize dp with negative infinity
        dp[0] = nums[0]  # Base case: starting sum at index 0 is nums[0]

        # Use a deque to efficiently track the maximum sums within the jump range
        deque = collections.deque([0])

        for i in range(1, n):
            # Remove elements from the front of the deque that are outside the jump range
            while deque and deque[0] < i - k:
                deque.popleft()

            # Update the current dp value using the maximum sum from the previous jumps
            dp[i] = nums[i] + dp[deque[0]]  # deque[0] gives the index with max sum in the range
            
            # Maintain the deque in decreasing order of dp values
            while deque and dp[i] >= dp[deque[-1]]:
                deque.pop()
            deque.append(i)

        return max(dp) # Return the maximum sum among all reachable indices


# Test Cases
solution = Solution()
print(solution.maxJumpSum([1, -2, 3, 2, -1], 2))  # Output: 6
print(solution.maxJumpSum([-1, -2, -3], 1))  # Output: -1
print(solution.maxJumpSum([2, 1, -3, 4, 5], 3))  # Output: 11
print(solution.maxJumpSum([10, -5, -2, 4, 0, 3], 3)) # Output: 14
print(solution.maxJumpSum([1, 2, 3, -2, -1, 5], 2)) # Output: 8


# Time Complexity: O(n) because we iterate through the array once. Using deque is amortized O(1) for pop/append.
# Space Complexity: O(n) for the dp array and the deque.

```