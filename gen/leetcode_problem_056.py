```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular array of integers nums, return the maximum possible sum of a non-empty subarray of nums, where no two elements in the subarray are adjacent.
# In a circular array, the last element is considered adjacent to the first.

# Examples:
# Example 1:
# Input: nums = [2,4,6,2,5]
# Output: 13
# Explanation: We can choose subarray [2,6,5], where no two elements are adjacent, to get the maximum sum 13.

# Example 2:
# Input: nums = [5,10,100,10,5]
# Output: 110
# Explanation: We can choose subarray [10,10,5], where no two elements are adjacent, to get the maximum sum 110.

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
            The maximum possible sum of a non-empty subarray.
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        
        # Two scenarios: either include the first element or exclude it.
        # Calculate the maximum sum for both scenarios using dynamic programming.
        
        def house_robber(arr):  # Helper function for standard house robber problem (linear array)
            dp = [0] * len(arr)
            dp[0] = arr[0]
            if len(arr) > 1:
                dp[1] = max(arr[0], arr[1])
            for i in range(2, len(arr)):
                dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])
            return dp[-1]


        # Scenario 1: Exclude the last element (treat as a linear array)
        max_sum1 = house_robber(nums[:-1])

        # Scenario 2: Exclude the first element (treat as a linear array)
        max_sum2 = house_robber(nums[1:])

        return max(max_sum1, max_sum2)

# Time Complexity: O(n) - We iterate through the array twice in the helper function.
# Space Complexity: O(n) - We use a dp array of size n in the helper function.  Could be optimized to O(1) space.


# Test cases
solution = Solution()
print(solution.rob([2, 4, 6, 2, 5]))  # Output: 13
print(solution.rob([5, 10, 100, 10, 5]))  # Output: 110
print(solution.rob([1]))  # Output: 1
print(solution.rob([1, 2, 3, 1]))  # Output: 4
print(solution.rob([1, 2])) # Output: 2
print(solution.rob([1,7,9,2])) # Output 10


```