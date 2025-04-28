```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular array of integers nums, return the maximum sum of a non-adjacent subset of elements. 
# "Non-adjacent" means no two elements in the subset are directly adjacent to each other in the circular array.
# Note that the last element and the first element are considered adjacent.

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
# 1 <= nums[i] <= 10^4
'''

class Solution:
    def rob(self, nums: list[int]) -> int:
        """
        Calculates the maximum sum of non-adjacent elements in a circular array.

        Args:
            nums: The circular array of integers.

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

        # We consider two scenarios:
        # 1. Excluding the last element (same as House Robber I)
        # 2. Excluding the first element

        def house_robber(arr):  # Helper function for House Robber I logic
            dp = [0] * len(arr)
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])
            for i in range(2, len(arr)):
                dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])
            return dp[-1]

        # Scenario 1: Exclude last element
        max1 = house_robber(nums[:-1])

        # Scenario 2: Exclude first element
        max2 = house_robber(nums[1:])

        return max(max1, max2)



# Test Cases
sol = Solution()

print(sol.rob([2, 7, 9, 3, 1]))  # Output: 11
print(sol.rob([1, 2, 3, 1]))  # Output: 4
print(sol.rob([1, 3, 1, 3, 100]))  # Output: 103
print(sol.rob([1]))  # Output: 1
print(sol.rob([1,2])) # Output: 2
print(sol.rob([])) # Output: 0



'''
Time Complexity: O(n), where n is the length of the input array. We iterate through the array twice in the house_robber function.

Space Complexity: O(n) for the dp array in the house_robber function.  This can be optimized to O(1) by using variables instead of an array to store previous results.
'''

```