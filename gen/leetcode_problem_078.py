```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular array of integers nums, find the maximum possible sum you can get 
# by selecting non-adjacent elements. The array is considered circular, meaning the 
# last element is adjacent to the first one.

# Examples:
# Example 1:
# Input: nums = [2, 4, 1, 3, 5]
# Output: 10
# Explanation: Select 4, 3, and 5.

# Example 2:
# Input: nums = [1, 2, 3, 1]
# Output: 4
# Explanation: Select 1 and 3.

# Example 3:
# Input: nums = [1]
# Output: 1
# Explanation: Select the only element

# Constraints:
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
'''

class Solution:
    def rob_circular(self, nums: list[int]) -> int:
        """
        Calculates the maximum sum of non-adjacent elements in a circular array.

        Uses dynamic programming to avoid redundant calculations.  We consider two scenarios:
        1. Robbing the first house: In this case, we can't rob the last house.
        2. Not robbing the first house: In this case, we can rob the last house.
        We calculate the maximum possible sum for both scenarios and return the larger one.


        Time Complexity: O(N) - We iterate through the array twice.
        Space Complexity: O(1) - Constant extra space.
        """
        n = len(nums)
        if n == 1:
            return nums[0]

        def rob_linear(arr):
            rob1, rob2 = 0, 0
            for num in arr:
                temp = max(num + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2


        # Scenario 1: Robbing the first house
        max1 = rob_linear(nums[:-1])

        # Scenario 2: Not robbing the first house
        max2 = rob_linear(nums[1:])

        return max(max1, max2)



# Test Cases
solution = Solution()

print(solution.rob_circular([2, 4, 1, 3, 5]))  # Output: 10
print(solution.rob_circular([1, 2, 3, 1]))  # Output: 4
print(solution.rob_circular([1]))  # Output: 1
print(solution.rob_circular([1, 3, 1, 3, 100]))  # Output: 103
print(solution.rob_circular([2,7,9,3,1])) # Output: 11




```