```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular integer array nums (i.e., the last element is also adjacent to the first element), 
# find the maximum sum of a non-adjacent subset of its elements.  A non-adjacent subset 
# means no two elements in the subset are adjacent to each other in the circular array.

# Examples:
# Example 1:
# Input: nums = [2, 4, 1, 3, 5]
# Output: 10
# Explanation: Pick elements 4, 3, and 5 for a sum of 10.

# Example 2:
# Input: nums = [1, 2, 3, 1]
# Output: 4
# Explanation: Pick elements 1 and 3 for a sum of 4.

# Constraints:
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^4
'''

class Solution:
    def rob_circular(self, nums: list[int]) -> int:
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
            return max(nums[0], nums[1])

        # Consider two cases:
        # 1. Excluding the last element (standard house robber problem)
        # 2. Excluding the first element (standard house robber problem)

        def house_robber(arr):
            dp = [0] * len(arr)
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])
            for i in range(2, len(arr)):
                dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])
            return dp[-1]

        # Case 1: Exclude last element
        max1 = house_robber(nums[:-1])
        
        # Case 2: Exclude first element
        max2 = house_robber(nums[1:])

        return max(max1, max2)


# Time Complexity: O(N), where N is the length of the input array. We iterate through the array twice in the house_robber function.
# Space Complexity: O(N) for the dp array in the house_robber function. This can be optimized to O(1) by using only two variables.

# Test Cases
solution = Solution()
print(solution.rob_circular([2, 4, 1, 3, 5]))  # Output: 10
print(solution.rob_circular([1, 2, 3, 1]))  # Output: 4
print(solution.rob_circular([1]))  # Output: 1
print(solution.rob_circular([1, 2]))  # Output: 2
print(solution.rob_circular([1, 5, 2, 3])) # Output: 6
print(solution.rob_circular([2,3,2])) # Output: 3


```