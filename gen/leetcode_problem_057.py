```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular integer array nums (i.e., the next element of nums[-1] is nums[0]), 
# return the maximum sum of a non-empty subsequence of nums such that no two elements in the subsequence are adjacent.

# Examples:
# Example 1:
# Input: nums = [2,1,3,7,5]
# Output: 12
# Explanation: Pick the subsequence [2, 3, 7], the sum is 12. [1, 5] is also a valid subsequence with sum 6, but 12 is the maximum.

# Example 2:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Pick the subsequence [2, 1], the sum is 4.

# Example 3:
# Input: nums = [1]
# Output: 1

# Constraints:
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
'''

class Solution:
    def rob(self, nums: list[int]) -> int:
        """
        Calculates the maximum sum of non-adjacent elements in a circular array.

        This problem is an extension of the classic House Robber problem but with a circular constraint.
        We use dynamic programming to solve it.  Since the last element can affect the first element's 
        inclusion (and vice-versa), we consider two scenarios:
        1. Include the first element, exclude the last.
        2. Exclude the first element, potentially include the last.
        We calculate the maximum sum for each scenario and return the overall maximum.

        Time Complexity: O(N) - We iterate through the array twice.
        Space Complexity: O(1) - We use constant extra space.

        Args:
            nums: The input circular integer array.

        Returns:
            The maximum sum of non-adjacent elements.
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        
        def rob_linear(arr):  # Helper function to solve the linear House Robber problem
            prev, curr = 0, 0
            for num in arr:
                prev, curr = curr, max(curr, prev + num)
            return curr

        # Scenario 1: Include first, exclude last
        max1 = rob_linear(nums[:-1])
        # Scenario 2: Exclude first, include last
        max2 = rob_linear(nums[1:])
        
        return max(max1, max2)


# Test Cases
solution = Solution()
print(solution.rob([2, 1, 3, 7, 5]))  # Output: 12
print(solution.rob([1, 2, 3, 1]))  # Output: 4
print(solution.rob([1]))  # Output: 1
print(solution.rob([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))  # Output: 15
print(solution.rob([-1, -2, -3])) # Output: -1

```