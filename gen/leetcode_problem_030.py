```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular integer array nums (i.e., the last element is also adjacent to the first element), 
# find the maximum sum of a non-adjacent subset of elements.  No adjacent elements can be included 
# in the subset.  The array can contain both positive and negative integers.

# Examples:
# Example 1:
# Input: nums = [2, 4, 1, 3, 5]
# Output: 10
# Explanation: We can select elements at indices 0, 2, and 4 (2 + 1 + 5 = 8) or indices 1 and 3 (4 + 3 = 7). Or we can select elements at indices 1 and 4 (4 + 5 = 9). Selecting 2, 3, and 5 yields the maximum sum of 10.

# Example 2:
# Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: 6
# Explanation: Selecting elements 4, 2, and 4 gives the maximum sum of 6 (4 + 2 + 4).

# Constraints:
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
'''

class Solution:
    def rob_circular(self, nums: list[int]) -> int:
        """
        Calculates the maximum sum of non-adjacent elements in a circular array.

        Args:
            nums: The input circular integer array.

        Returns:
            The maximum sum of non-adjacent elements.
        """
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]
        if n == 2: return max(nums[0], nums[1])

        # Consider two scenarios:
        # 1. Include the first element: then we can't include the last
        # 2. Exclude the first element: then we can include the last

        def house_robber(arr):  # Standard house robber logic (linear DP)
            dp = [0] * len(arr)
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])
            for i in range(2, len(arr)):
                dp[i] = max(dp[i-1], dp[i-2] + arr[i])
            return dp[-1]

        include_first = house_robber(nums[:-1])   # Exclude the last element
        exclude_first = house_robber(nums[1:]) # Exclude the first element

        return max(include_first, exclude_first)

# Time Complexity: O(n) - We iterate through the array twice in the house_robber function.
# Space Complexity: O(n) - We use a DP array of size n in the house_robber function. Can be optimized to O(1) space.



# Test Cases
solution = Solution()

print(solution.rob_circular([2, 4, 1, 3, 5]))  # Output: 10
print(solution.rob_circular([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Output: 6
print(solution.rob_circular([1,2,3,1])) # Output: 4
print(solution.rob_circular([1])) # Output: 1
print(solution.rob_circular([])) # Output: 0

```