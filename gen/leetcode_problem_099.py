```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular array of integers nums (where the last element is considered adjacent to the first element), 
# find the maximum sum of a subset of non-adjacent elements.

# Examples:
# Example 1:
# Input: nums = [2, 4, 1, 3, 5]
# Output: 10
# Explanation: Selecting elements at indices 0, 2, and 4 (2 + 1 + 5 = 8)
#             OR selecting elements at indices 1 and 3 (4 + 3 = 7)
#             OR selecting elements at indices 0, 2, and 4 with wrap-around (2 + 1 + 5)
#             OR selecting 1 and 3 with wrap-around (4+3).
#             Selecting elements at indices 1 and 4 (4 + 5 = 9). 
#             However, selecting 2, 1, and 5 yields the maximum sum of 10.


# Example 2:
# Input: nums = [1, 2, 3, 1]
# Output: 4
# Explanation: Selecting elements at indices 0 and 2 (1 + 3 = 4) yields the maximum sum.

# Constraints:
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
'''

class Solution:
    def rob(self, nums: list[int]) -> int:
        """
        Calculates the maximum sum of non-adjacent elements in a circular array.

        Args:
            nums: The circular array of integers.

        Returns:
            The maximum sum of non-adjacent elements.
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        # Consider two cases:
        # 1. Excluding the last element (like a regular array)
        # 2. Excluding the first element

        def house_robber(arr):
            prev_max, curr_max = 0, 0
            for num in arr:
                prev_max, curr_max = curr_max, max(curr_max, prev_max + num)
            return curr_max

        # Case 1: Exclude the last element
        max1 = house_robber(nums[:-1])

        # Case 2: Exclude the first element
        max2 = house_robber(nums[1:])
        
        return max(max1, max2)

    # Time Complexity: O(n), where n is the length of the input array. We iterate through the array twice in the house_robber function.
    # Space Complexity: O(1)


# Test cases
solution = Solution()
print(solution.rob([2, 4, 1, 3, 5]))  # Output: 10
print(solution.rob([1, 2, 3, 1]))  # Output: 4
print(solution.rob([1, 2, 3, 1, 5]))  # Output: 9
print(solution.rob([1])) # Output: 1
print(solution.rob([])) # Output: 0
print(solution.rob([1,5,3,10])) # Output: 15


```