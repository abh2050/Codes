```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular array of integers nums (where the last element is considered adjacent to the first element), 
# find the maximum sum of a subset of non-adjacent elements.

# Examples:
# Example 1:
# Input: nums = [2, 7, 9, 3, 1]
# Output: 11
# Explanation: Pick nums[0], nums[2], and nums[4] for a sum of 2 + 9 + 1 = 11.

# Example 2:
# Input: nums = [1, 2, 3, 1]
# Output: 4
# Explanation: Pick nums[0] and nums[2] for a sum of 1 + 3 = 4.

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
            The maximum sum of non-adjacent elements.
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        
        # Consider two scenarios: either include the first element or exclude it.
        # 1. Include first element: Can't include last element. Equivalent to robbing a linear array nums[:-1]
        # 2. Exclude first element: Can include last element. Equivalent to robbing a linear array nums[1:]
        
        def rob_linear(arr):
            n = len(arr)
            dp = [0] * n
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])
            for i in range(2, n):
                dp[i] = max(dp[i-1], dp[i-2] + arr[i]) # Either skip current or take current + best of two steps back
            return dp[n-1]
            
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))



# Test Cases
solution = Solution()

print(f"Input: [2, 7, 9, 3, 1], Output: {solution.rob([2, 7, 9, 3, 1])}, Expected: 11")  # Example 1
print(f"Input: [1, 2, 3, 1], Output: {solution.rob([1, 2, 3, 1])}, Expected: 4")  # Example 2
print(f"Input: [1], Output: {solution.rob([1])}, Expected: 1") # Single element
print(f"Input: [1,2], Output: {solution.rob([1,2])}, Expected: 2")  # Two elements
print(f"Input: [1,2,3,4,5,1,2,3,4,5], Output: {solution.rob([1,2,3,4,5,1,2,3,4,5])}, Expected: 16") # Larger Example

'''
Time Complexity: O(n) - We iterate through the array twice in the worst case (once for each subproblem).
Space Complexity: O(n) -  We use an array of size 'n' for dynamic programming in the rob_linear helper function.  Could be optimized to O(1) space by using variables to store only the last two DP values.
'''


```