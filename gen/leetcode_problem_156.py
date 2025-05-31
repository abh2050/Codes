```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular integer array nums, return the maximum possible sum of a non-empty subarray of nums, where no two elements in the subarray are adjacent.

# Examples:
# Example 1:
# Input: nums = [2,1,4,9]
# Output: 11
# Explanation: Choosing elements 2 and 9 yields the maximum sum 11. 

# Example 2:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Choosing elements 1 and 3 yields the maximum sum 4.

# Example 3:
# Input: nums = [1]
# Output: 1
# Explanation: Choosing the single element yields the maximum sum 1.

# Constraints:
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
'''

class Solution:
    def rob(self, nums: list[int]) -> int:
        """
        Calculates the maximum sum of non-adjacent elements in a circular array.

        This problem is a variation of the House Robber II problem. The circular nature means we
        can't rob both the first and last houses simultaneously. We handle this by considering two
        scenarios:
        1. Robbing the first house and excluding the last.
        2. Robbing the last house and excluding the first.
        We then take the maximum of the two scenarios.

        Time Complexity: O(n) - We iterate through the array twice.
        Space Complexity: O(1) - We use constant extra space.
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        
        def rob_linear(arr):
            """Helper function to rob a linear array (non-circular)."""
            rob1, rob2 = 0, 0
            for num in arr:
                temp = max(num + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        
        # Scenario 1: Exclude last house
        scenario1 = rob_linear(nums[:-1])
        
        # Scenario 2: Exclude first house
        scenario2 = rob_linear(nums[1:])
        
        return max(scenario1, scenario2)


# Test cases
solution = Solution()

print(solution.rob([2, 1, 4, 9]))  # Output: 11
print(solution.rob([1, 2, 3, 1]))  # Output: 4
print(solution.rob([1]))  # Output: 1
print(solution.rob([1, 2, 3])) # Output: 4
print(solution.rob([1,7,9,2])) # Output: 10



```