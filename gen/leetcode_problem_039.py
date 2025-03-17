```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular array of integers nums (meaning the last element is adjacent to the first), 
# find the maximum sum of a subset of its elements where no two adjacent elements in the 
# original array (including the first and last elements) are selected.

# Examples:
# Example 1:
# Input: nums = [2, 1, 4, 9]
# Output: 11
# Explanation: We can select 2 and 9 for a total of 11.  1 and 4 are adjacent so we can only pick one.

# Example 2:
# Input: nums = [1, 2, 3, 1]
# Output: 4
# Explanation: We can select 1 and 3 for a total of 4.

# Example 3:
# Input: nums = [1]
# Output: 1
# Explanation: We select the only element.

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
            The maximum sum of non-adjacent elements.
        """
        n = len(nums)
        if n == 1:
            return nums[0]

        # Consider two scenarios:
        # 1. Robbing the first house but not the last
        # 2. Not robbing the first house but possibly the last

        def rob_linear(arr):
            """Helper function to calculate max sum for a linear array (House Robber I)."""
            rob1, rob2 = 0, 0
            for num in arr:
                new_rob = max(rob1 + num, rob2)
                rob1 = rob2
                rob2 = new_rob
            return rob2


        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))


# Time Complexity: O(N) - We iterate through the array twice in the rob_linear function.
# Space Complexity: O(1) - We only use constant extra space.



# Test Cases
solution = Solution()
print(solution.rob_circular([2, 1, 4, 9]))  # Output: 11
print(solution.rob_circular([1, 2, 3, 1]))  # Output: 4
print(solution.rob_circular([1]))  # Output: 1
print(solution.rob_circular([1, 3, 1, 3, 100])) # Output 103
print(solution.rob_circular([2,7,9,3,1])) # Output 11




```