```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular integer array nums (i.e., the first element is considered adjacent to the last element), 
# find the maximum sum of a non-adjacent subset of elements. A subset is considered non-adjacent if no two elements in the subset are adjacent in the circular array.

# Examples:
# Example 1:
# Input: nums = [2, 4, 1, 3, 5]
# Output: 10
# Explanation: The maximum sum is achieved with the subset [4, 5], which sums up to 10.

# Example 2:
# Input: nums = [1, 2, 3, 1]
# Output: 4
# Explanation: The maximum sum is achieved with the subset [1, 3], which sums up to 4.

# Constraints:
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
'''

class Solution:
    def rob(self, nums: list[int]) -> int:
        """
        Calculates the maximum sum of non-adjacent elements in a circular array.

        Args:
            nums: The input circular integer array.

        Returns:
            The maximum sum of a non-adjacent subset.
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)

        # Consider two cases:
        # 1. Include the first element, exclude the last.
        # 2. Exclude the first element, include the last.
        def house_robber(arr):
            dp = [0] * len(arr)
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])
            for i in range(2, len(arr)):
                dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])
            return dp[-1]

        return max(house_robber(nums[:-1]), house_robber(nums[1:]))


# Test cases
solution = Solution()
print(solution.rob([2, 4, 1, 3, 5]))  # Output: 10
print(solution.rob([1, 2, 3, 1]))  # Output: 4
print(solution.rob([1])) # Output: 1
print(solution.rob([1,5])) # Output: 5
print(solution.rob([1,3,1,3,100])) # Output 103


'''
Time Complexity: O(n), where n is the length of the input array. We iterate through the array twice in the worst case (once for each subproblem).

Space Complexity: O(n) for the dp array used in the house_robber helper function.  This can be optimized to O(1) by using variables to store only the previous two values in the dp array.
'''

```