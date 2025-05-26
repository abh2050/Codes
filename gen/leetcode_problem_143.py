```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular integer array nums (i.e., the next element of nums[-1] is nums[0]),
# return the maximum sum of a non-adjacent subsequence. A non-adjacent subsequence 
# is a subsequence where no two elements are adjacent in the original circular array.

# Examples:
# Example 1:
# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot choose both 2 and 3. So you either choose 2 or 3.

# Example 2:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: You can choose 1 and 3 for a total sum of 4.

# Example 3:
# Input: nums = [1,15,3,6,2]
# Output: 18
# Explanation: You can choose 15 and 3, or 15 and 2, for a total sum of 18.

# Constraints:
# 1 <= nums.length <= 10^5
# -3 * 10^4 <= nums[i] <= 3 * 10^4
'''

class Solution:
    def rob(self, nums: list[int]) -> int:
        """
        Calculates the maximum sum of non-adjacent elements in a circular array.

        Args:
            nums: The input circular integer array.

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
        # 1. nums[0] is included: then we can't include nums[n-1], and the problem reduces to house robber I on nums[0:n-1].
        # 2. nums[0] is excluded: then we can include nums[n-1], and the problem reduces to house robber I on nums[1:n].

        def house_robber_i(arr):
            """Helper function to solve the standard house robber problem (non-circular)."""
            n = len(arr)
            dp = [0] * n
            dp[0] = arr[0]
            if n > 1:
                dp[1] = max(arr[0], arr[1])
            for i in range(2, n):
                dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])  # either skip current or rob it
            return dp[n - 1]

        return max(house_robber_i(nums[:-1]), house_robber_i(nums[1:]))


# Test cases
solution = Solution()
print(solution.rob([2, 3, 2]))  # Output: 3
print(solution.rob([1, 2, 3, 1]))  # Output: 4
print(solution.rob([1, 15, 3, 6, 2]))  # Output: 18
print(solution.rob([1]))  # Output: 1
print(solution.rob([1, 2]))  # Output: 2
print(solution.rob([1, 2, 1, 1])) # Output: 3

```


**Explanation:**

The solution leverages the standard House Robber problem (non-circular).  By considering two scenarios (including or excluding the first element of the circular array), we transform the circular problem into two standard House Robber problems. The `house_robber_i` helper function uses dynamic programming to efficiently solve the standard House Robber problem in linear time.

**Time and Space Complexity:**

* **Time Complexity:** O(n), where n is the length of the input array `nums`. This is because we iterate through the array twice in the worst case (once for each subproblem).
* **Space Complexity:** O(n) for the dynamic programming array in `house_robber_i`. This can be optimized to O(1) by using only two variables to store the previous two maximum sums. However, for clarity, the O(n) solution is presented here.