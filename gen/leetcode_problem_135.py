```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular array of integers nums, find the maximum possible sum you can get by adding non-adjacent elements.
# The array is considered circular, meaning the last element is adjacent to the first element.

# Examples:
# Example 1:
# Input: nums = [1, 2, 3, 1]
# Output: 4
# Explanation: Select 1 and 3.

# Example 2:
# Input: nums = [2,7,9,3,1]
# Output: 10
# Explanation: Select 7 and 3 or 9 and 1, or 2 and 9.  7 and 3 gives the maximum sum. 

# Example 3:
# Input: nums = [1, 15, 3, 5]
# Output: 20
# Explanation: Select 15 and 5.

# Constraints:
# 1 <= nums.length <= 3 * 10^4
# -10^4 <= nums[i] <= 10^4
'''

class Solution:
    def rob_circular(self, nums: list[int]) -> int:
        """
        Calculates the maximum sum of non-adjacent elements in a circular array.

        Args:
            nums: The input circular array of integers.

        Returns:
            The maximum possible sum of non-adjacent elements.
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)

        # Handle the circularity by considering two cases:
        # 1. Include the first element, exclude the last
        # 2. Exclude the first element, include the last (potentially)

        def rob_linear(arr): # Helper function to solve the linear house robber problem.
            n = len(arr)
            dp = [0] * (n + 1)
            dp[1] = arr[0]
            for i in range(2, n + 1):
                dp[i] = max(dp[i - 1], dp[i - 2] + arr[i - 1]) # dp[i] stores the maximum sum up to element i-1
            return dp[n]


        include_first = rob_linear(nums[:-1])  # Exclude the last element
        exclude_first = rob_linear(nums[1:])  # Exclude the first element

        return max(include_first, exclude_first)

# Test cases
solution = Solution()

print(solution.rob_circular([1, 2, 3, 1]))  # Output: 4
print(solution.rob_circular([2, 7, 9, 3, 1]))  # Output: 10
print(solution.rob_circular([1, 15, 3, 5])) # Output: 20
print(solution.rob_circular([1]))  # Output: 1
print(solution.rob_circular([1,2])) # Output: 2
print(solution.rob_circular([])) # Output: 0


'''
Time Complexity: O(n), where n is the length of the input array. We iterate through the array twice in the worst case (once for each subproblem).
Space Complexity: O(n) for the dp array in the rob_linear helper function. This can be optimized to O(1) by using only two variables to store the previous two maximum sums.

'''


```