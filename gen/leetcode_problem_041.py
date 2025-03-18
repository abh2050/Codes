```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular array of integers nums, return the maximum sum of a non-adjacent subsequence. 
# In a circular array, the last element is considered adjacent to the first element.  A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

# Examples:
# Example 1:
# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot choose both 2 and 2, so you must pick only one of the 2's. Choosing only the 3 and leaving the 2's results in the maximum sum.

# Example 2:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Choose 1, 3 and skip the 2 and last 1. 1 + 3 = 4 which is the maximum sum.

# Example 3:
# Input: nums = [1,15,3,2,10,5]
# Output: 25
# Explanation: Choose 15, 10, which sum to 25

# Constraints:
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^4
'''

class Solution:
    def rob_circular(self, nums: list[int]) -> int:
        """
        Calculates the maximum sum of non-adjacent elements in a circular array.

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
        if n == 2:
            return max(nums)

        # We consider two scenarios:
        # 1. Rob the first house, then we can't rob the last house.
        # 2. Don't rob the first house, then we can rob the last house.
        # The maximum of these two scenarios is the answer.

        def house_robber(arr): # Helper function to solve standard house robber problem
            n = len(arr)
            dp = [0] * n
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])
            for i in range(2, n):
                dp[i] = max(dp[i-1], dp[i-2] + arr[i])
            return dp[n-1]

        # Scenario 1: Include the first element, exclude the last
        max1 = house_robber(nums[:-1])

        # Scenario 2: Exclude the first element, include the last
        max2 = house_robber(nums[1:])
        
        return max(max1, max2)


# Test cases
solution = Solution()
print(solution.rob_circular([2, 3, 2]))  # Output: 3
print(solution.rob_circular([1, 2, 3, 1]))  # Output: 4
print(solution.rob_circular([1,15,3,2,10,5])) # Output: 25
print(solution.rob_circular([1]))  # Output: 1
print(solution.rob_circular([1,2]))  # Output: 2
print(solution.rob_circular([]))  # Output: 0


"""
Time Complexity: O(N), where N is the length of the input array. We iterate through the array twice in the worst case in the house_robber helper function.

Space Complexity: O(N) for the dp array in the house_robber helper function.  This can be optimized to O(1) by using variables to store the previous two values instead of the entire dp array.
"""

```