```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular array of integers nums, find the maximum possible sum you can get by adding non-adjacent elements. 
# In a circular array, the first and last elements are considered adjacent.

# Examples:
# Example 1:
# Input: nums = [1, 2, 3, 1]
# Output: 4
# Explanation: Select 1 and 3.

# Example 2:
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Select 2, 9, and 1.

# Example 3:
# Input: nums = [1, 15, 3, 2, 10]
# Output: 25
# Explanation: Select 15 and 10.

# Constraints:
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^3
'''

class Solution:
    def rob(self, nums: list[int]) -> int:
        """
        Calculates the maximum sum of non-adjacent elements in a circular array.

        Args:
            nums: The input circular array of integers.

        Returns:
            The maximum possible sum.
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)

        # Consider two scenarios:
        # 1. Include the first element, exclude the last
        # 2. Exclude the first element, include the last (potentially)

        def house_robber(arr):
            """Helper function implementing House Robber I logic (linear array)."""
            rob1, rob2 = 0, 0
            for num in arr:
                temp = max(num + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2


        include_first = house_robber(nums[:-1])  # Scenario 1
        exclude_first = house_robber(nums[1:])  # Scenario 2

        return max(include_first, exclude_first)


    # Time Complexity: O(N) - We iterate through the array twice in the helper function.
    # Space Complexity: O(1) - Constant extra space is used.



# Test Cases
solution = Solution()
print(solution.rob([1, 2, 3, 1]))  # Output: 4
print(solution.rob([2, 7, 9, 3, 1]))  # Output: 12
print(solution.rob([1, 15, 3, 2, 10])) # Output 25
print(solution.rob([1]))  # Output: 1
print(solution.rob([1,2])) # Output: 2
print(solution.rob([1,10,1,1,10])) # Output: 20



```
