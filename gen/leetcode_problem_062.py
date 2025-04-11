```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular array of integers nums (where the first element is considered adjacent to the last), 
# find the maximum sum of a non-adjacent subset of elements.  A subset is "non-adjacent" if no two elements in the subset 
# are adjacent to each other in the original array (including the first and last elements being considered adjacent).


# Examples:
# Example 1:
# Input: nums = [2, 4, 1, 3, 5]
# Output: 10
# Explanation: The maximum sum can be achieved by selecting [4, 5] or [2, 3, 5].

# Example 2:
# Input: nums = [1, 2, 3, 1]
# Output: 4
# Explanation: The maximum sum can be achieved by selecting [1, 3].

# Example 3:
# Input: nums = [1]
# Output: 1


# Constraints:
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^4
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
        if n == 0: return 0
        if n == 1: return nums[0]
        if n == 2: return max(nums)


        def rob_linear(arr):  # Helper function for the linear house robber problem
            n = len(arr)
            dp = [0] * n
            dp[0] = arr[0]
            if n > 1:
                dp[1] = max(arr[0], arr[1])
            for i in range(2, n):
                dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])
            return dp[n - 1]


        # Consider two scenarios:
        # 1. Excluding the last element (linear rob from 0 to n-2)
        # 2. Excluding the first element (linear rob from 1 to n-1)
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))



    '''
    Time Complexity: O(n) - We traverse the array twice in the rob_linear function.
    Space Complexity: O(n) - We use a DP array of size n in the rob_linear function.
                         However, this can be optimized to O(1) space by using only two variables 
                         to store the previous two DP values.
    '''



# Test Cases
solution = Solution()
print(solution.rob_circular([2, 4, 1, 3, 5]))  # Output: 10
print(solution.rob_circular([1, 2, 3, 1]))  # Output: 4
print(solution.rob_circular([1])) # Output: 1
print(solution.rob_circular([1,2])) # Output: 2
print(solution.rob_circular([1,7,9,2])) # Output: 10
```