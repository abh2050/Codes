```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular array of integers nums, find the maximum sum of a non-adjacent subset of elements.
# In a circular array, the first and last elements are considered adjacent.

# Examples:
# Example 1:
# Input: nums = [2, 7, 9, 3, 1]
# Output: 11
# Explanation: Pick nums[0] (2), nums[2] (9), and nums[4] (1). The sum is 11.

# Example 2:
# Input: nums = [1, 2, 3, 1]
# Output: 4
# Explanation: Pick nums[0] (1) and nums[2] (3). The sum is 4.

# Constraints:
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
'''

class Solution:
    def rob_circular(self, nums: list[int]) -> int:
        """
        Calculates the maximum sum of non-adjacent elements in a circular array.

        Args:
            nums: The input circular array of integers.

        Returns:
            The maximum sum of non-adjacent elements.
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        # Handle circularity by calculating max sum excluding the first element and last element separately.
        def rob_linear(arr):  # Helper function for linear (non-circular) case. This is standard House Robber.
            n = len(arr)
            if n == 0: return 0
            if n == 1: return arr[0]
            dp = [0] * n
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])

            for i in range(2, n):
                dp[i] = max(dp[i-1], dp[i-2] + arr[i])
            return dp[n-1]

        # Exclude first element
        max1 = rob_linear(nums[1:])
        # Exclude last element
        max2 = rob_linear(nums[:-1])

        return max(max1, max2)

# Time Complexity: O(N), where N is the length of the input array.  We iterate through the array twice in the helper function
# Space Complexity: O(N) to store the dp array in the helper function. Can be optimized to O(1) with variables instead of dp array.



# Test cases
solution = Solution()
print(solution.rob_circular([2, 7, 9, 3, 1]))  # Output: 11
print(solution.rob_circular([1, 2, 3, 1]))  # Output: 4
print(solution.rob_circular([1])) # Output: 1
print(solution.rob_circular([])) # Output: 0
print(solution.rob_circular([1, 2])) # Output: 2 (Not 3 because they're adjacent in circular array)
print(solution.rob_circular([1,3,1,3,100])) # Output 103
```