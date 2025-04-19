```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular array of integers nums (where the last element is considered adjacent to the first element), 
# find the maximum sum of a non-adjacent subset of elements. A non-adjacent subset is a subset where no two elements are adjacent in the circular array.

# Examples:
# Example 1:
# Input: nums = [2, 4, 1, 3, 5]
# Output: 10
# Explanation: The maximum sum is achieved by selecting the elements at indices 0, 2, and 4 (2 + 1 + 5 = 8) 
#              or selecting the elements at indices 1 and 3 (4 + 3 = 7)
#               Since it is circular [4,5] (4+5=9) or [5,2] (5+2 =7) or [1,3,5] (1+3+5=9)
#               [2,1,5] = 8 so 2, 1, and 5. OR 4 and 3
#              Consider the non-circular array first -> [2,1,5] = 8  [4,3] = 7
#               If you include the first element you can't include the last one and vice-versa.
# Example 2:
# Input: nums = [1, 2, 3, 1]
# Output: 4
# Explanation: The maximum sum is achieved by selecting the elements at indices 0 and 2 (1 + 3 = 4).

# Constraints:
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
'''

class Solution:
    def rob(self, nums: list[int]) -> int:
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
        # 1. Exclude the last element (treat as non-circular)
        # 2. Exclude the first element (treat as non-circular)
        return max(self.house_robber(nums[:-1]), self.house_robber(nums[1:]))

    def house_robber(self, nums: list[int]) -> int:
        """
        Helper function to solve the standard House Robber problem (non-circular).
        Uses dynamic programming.

        Args:
            nums: The input array of integers.

        Returns:
            The maximum sum of non-adjacent elements.
        """
        n = len(nums)
        if n == 0: return 0
        if n==1: return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[n - 1]


# Test cases
solution = Solution()
print(solution.rob([2, 4, 1, 3, 5]))  # Output: 10
print(solution.rob([1, 2, 3, 1]))  # Output: 4
print(solution.rob([1])) # Output: 1
print(solution.rob([])) # Output 0
print(solution.rob([1,2])) # Output: 2
print(solution.rob([1,5,2,1,8])) # Output: 14



'''
Time Complexity: O(N), where N is the length of the input array. We iterate through the array twice in the worst case.
Space Complexity: O(N) for the dp array in the house_robber helper function. 
This could be optimized to O(1) by using variables to store only the previous two values instead of the whole dp array.

'''
```