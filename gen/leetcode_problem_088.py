```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular integer array nums (i.e., the next element of nums[-1] is nums[0]), return the maximum sum of a non-empty subsequence of nums such that no two elements in the subsequence are adjacent in the circular array.

# Examples:
# Example 1:
# Input: nums = [2,1,4,9]
# Output: 11
# Explanation: We can select [2, 9] to get a maximum sum of 11. Notice that 2 and 9 are not adjacent since the array is circular.

# Example 2:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Selecting [1,3] gives us a sum of 4.

# Example 3:
# Input: nums = [1]
# Output: 1

# Constraints:
# 1 <= nums.length <= 3 * 10^4
# -3 * 10^4 <= nums[i] <= 3 * 10^4
'''

class Solution:
    def rob(self, nums: list[int]) -> int:
        """
        Calculates the maximum sum of non-adjacent elements in a circular array.

        Args:
            nums: The input circular integer array.

        Returns:
            The maximum sum.
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        
        # Consider two scenarios:
        # 1. Robbing the first house (excluding the last)
        # 2. Robbing the last house (excluding the first)
        # Return the maximum of these two scenarios.
        
        def rob_linear(arr):
            """Helper function for calculating max sum in a linear array (House Robber I logic)."""
            rob1, rob2 = 0, 0
            for num in arr:
                temp = max(rob1 + num, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))


# Test Cases
solution = Solution()
print(solution.rob([2, 1, 4, 9]))  # Output: 11
print(solution.rob([1, 2, 3, 1]))  # Output: 4
print(solution.rob([1]))  # Output: 1
print(solution.rob([1, 7, 9, 2])) # Output: 10
print(solution.rob([2,7,9,3,1])) # Output: 11

'''
Time Complexity: O(N), where N is the length of the input array. We iterate through the array twice in the worst case.
Space Complexity: O(1). We use constant extra space.
'''

```