```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular array of integers nums, return the maximum sum of a non-adjacent 
# subset of elements.  "Circular" means the last element and the first element are 
# considered adjacent.

# Examples:
# Example 1:
# Input: nums = [2, 7, 9, 3, 1]
# Output: 11
# Explanation: Pick nums[0], nums[2], nums[4]. (2 + 9 + 1 = 12) or Pick nums[1], nums[3]. (7 + 3 = 10). Maximum is 11 obtained by picking nums[1] and nums[3].
# Or pick nums[0], nums[2] and nums[4] which sums up to 11.


# Example 2:
# Input: nums = [1, 2, 3, 1]
# Output: 4
# Explanation: Pick nums[0] and nums[2] (1 + 3 = 4).

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

        # Consider two scenarios:
        # 1. Include the first element, exclude the last.
        # 2. Exclude the first element, include the last.

        def house_robber(arr):  # Helper function for standard house robber problem (linear)
            dp = [0] * len(arr)
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])
            for i in range(2, len(arr)):
                dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])
            return dp[-1]

        # Scenario 1: Exclude the last element.
        max1 = house_robber(nums[:-1])


        # Scenario 2: Exclude the first element.
        max2 = house_robber(nums[1:])

        return max(max1, max2)

# Time Complexity: O(N) - Two passes through the array using the helper function.
# Space Complexity: O(N) - For the dp array in the helper function.



# Test cases
sol = Solution()
print(sol.rob([2, 7, 9, 3, 1]))  # Output: 11
print(sol.rob([1, 2, 3, 1]))  # Output: 4
print(sol.rob([1,2,3])) #Output: 3
print(sol.rob([1]))  # Output: 1
print(sol.rob([1, 5])) # Output: 5
print(sol.rob([20,50,1,1,20])) # Output: 70

```