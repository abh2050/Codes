```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular integer array nums (i.e., the last element is also adjacent to the first element), 
# find the maximum sum of a non-adjacent subsequence. A non-adjacent subsequence is a subsequence 
# where no two elements are adjacent in the original circular array.

# Examples:
# Example 1:
# Input: nums = [2, 1, 4, 9]
# Output: 11
# Explanation: The maximum sum is obtained by selecting elements at indices 0 and 3 (2 + 9 = 11).

# Example 2:
# Input: nums = [1, 2, 3, 1]
# Output: 4
# Explanation: The maximum sum is obtained by selecting elements at indices 0 and 2 (1 + 3 = 4).


# Constraints:
# 1 <= nums.length <= 2 * 10^4
# -10^4 <= nums[i] <= 10^4
'''

class Solution:
    def rob_circular(self, nums: list[int]) -> int:
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

        # Consider two scenarios:
        # 1. Include the first element, exclude the last
        # 2. Exclude the first element, include the last

        # Helper function to calculate max sum for a linear array (House Robber I logic)
        def rob_linear(arr):
            n = len(arr)
            if n == 0:
                return 0
            if n == 1:
                return arr[0]

            dp = [0] * n
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])

            for i in range(2, n):
                dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])

            return dp[n - 1]

        # Scenario 1: Include first, exclude last
        max1 = rob_linear(nums[:-1])

        # Scenario 2: Exclude first, include last
        max2 = rob_linear(nums[1:])

        return max(max1, max2)



# Time Complexity: O(n), where n is the length of the input array. We iterate through the array twice in the rob_linear function.
# Space Complexity: O(n) for the dp array in the rob_linear function. This can be optimized to O(1) by using only two variables to track the previous two maximum sums.


# Test Cases
solution = Solution()

# Test Case 1
nums1 = [2, 1, 4, 9]
print(f"Test Case 1: {solution.rob_circular(nums1)}")  # Expected Output: 11

# Test Case 2
nums2 = [1, 2, 3, 1]
print(f"Test Case 2: {solution.rob_circular(nums2)}")  # Expected Output: 4

# Test Case 3 - Empty Array
nums3 = []
print(f"Test Case 3: {solution.rob_circular(nums3)}") # Expected Output: 0

# Test Case 4 - Single Element Array
nums4 = [5]
print(f"Test Case 4: {solution.rob_circular(nums4)}") # Expected Output: 5

# Test Case 5 - Two Element Array
nums5 = [1,2]
print(f"Test Case 5: {solution.rob_circular(nums5)}") # Expected Output: 2

# Test Case 6
nums6 = [1, 3, 1, 3, 100]
print(f"Test Case 6: {solution.rob_circular(nums6)}")  # Expected Output: 103
```