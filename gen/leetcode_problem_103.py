```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular array of integers nums (where the last element is considered adjacent to the first), 
# find the maximum sum of a non-adjacent subset of elements.  A subset is non-adjacent if no two elements 
# in the subset are adjacent in the circular array.

# Examples:
# Example 1:
# Input: nums = [2, 7, 9, 3, 1]
# Output: 11
# Explanation: Pick the elements at indices 0, 2, and 4 (2 + 9 + 1 = 12).  Alternatively, pick the elements at indices 1 and 3 (7+3=10).
# Since the array is circular index 0 and 4 are also considered adjacent. The optimal subset here is {7,9} or {2,9,1} with a sum of 11.


# Example 2:
# Input: nums = [1, 2, 3, 1]
# Output: 4
# Explanation: Pick elements at indices 0 and 2 (1 + 3 = 4).

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
            The maximum sum of a non-adjacent subset.
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)

        # Consider two scenarios:
        # 1. Robbing the first house: Exclude the last house.
        # 2. Not robbing the first house: Include the last house.
        return max(self.rob_linear(nums[:-1]), self.rob_linear(nums[1:]))

    def rob_linear(self, nums: list[int]) -> int:
        """
        Helper function to calculate the maximum sum of non-adjacent elements in a linear array
        (standard House Robber problem using dynamic programming).

        Args:
            nums: The input linear array of integers.

        Returns:
            The maximum sum of a non-adjacent subset.
        """
        n = len(nums)

        if not nums: return 0
        if n==1: return nums[0]


        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])


        for i in range(2,n):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        return dp[-1]



# Test Cases
solution = Solution()
print(solution.rob_circular([2, 7, 9, 3, 1]))  # Output: 11
print(solution.rob_circular([1, 2, 3, 1]))  # Output: 4
print(solution.rob_circular([1])) # Output: 1
print(solution.rob_circular([1,5])) # Output: 5
print(solution.rob_circular([1,3,1,3,100]))  #Output: 103


# Time Complexity: O(n) - We iterate through the array twice in rob_linear.
# Space Complexity: O(n) - for the dp array in rob_linear.  Could be optimized to O(1) by using variables to 
#                             track only the previous two values instead of the whole dp array.

```