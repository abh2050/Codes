```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular array of integers nums (where the last element is considered adjacent to the first element), 
# find the maximum sum of a non-adjacent subset of elements.  A subset is "non-adjacent" if no two elements in the subset are adjacent in the circular array.

# Examples:
# Example 1:
# Input: nums = [2, 1, 4, 9]
# Output: 11
# Explanation: We can select elements at indices 0 and 3 (2 + 9 = 11).  Or we can select elements at indices 1 and 2 (1 + 4 = 5). 11 is the maximum sum.

# Example 2:
# Input: nums = [1, 2, 3, 1]
# Output: 4
# Explanation: We can select elements at indices 0 and 2 (1 + 3 = 4).

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
        if n == 2:
            return max(nums)

        # Consider two cases:
        # 1. Exclude the last element:  Standard house robber problem on nums[:-1]
        # 2. Exclude the first element: Standard house robber problem on nums[1:]
        # Return the maximum of these two cases.

        def house_robber(arr):
            """Helper function for standard house robber problem (linear array)."""
            n = len(arr)
            dp = [0] * n
            dp[0] = arr[0]
            if n > 1:
                dp[1] = max(arr[0], arr[1])
            for i in range(2, n):
                dp[i] = max(dp[i-1], dp[i-2] + arr[i])  # Either skip current or include it (and skip previous)
            return dp[-1]

        return max(house_robber(nums[:-1]), house_robber(nums[1:]))

# Time Complexity: O(N), where N is the length of the array. We perform two linear scans using the house_robber helper.
# Space Complexity: O(N) in the current implementation due to the dp array in house_robber. This could be optimized to O(1) by only storing the previous two dp values.



# Test Cases
solution = Solution()
print(solution.rob_circular([2, 1, 4, 9]))  # Output: 11
print(solution.rob_circular([1, 2, 3, 1]))  # Output: 4
print(solution.rob_circular([1, 2, 3, 1, 5])) # Output: 8
print(solution.rob_circular([1]))  # Output: 1
print(solution.rob_circular([1, 2])) # Output: 2
print(solution.rob_circular([])) # Output: 0

```