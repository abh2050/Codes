```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular array of integers nums (where the first element is considered adjacent to the last element), 
# find the maximum sum of a non-adjacent subsequence. A non-adjacent subsequence is a subsequence where no two 
# selected elements are adjacent in the circular array.

# Examples:
# Example 1:
# Input: nums = [2, 4, 1, 3, 5]
# Output: 10
# Explanation: Selecting elements 2, 1, and 5 yields the maximum sum (2 + 1 + 5 = 8).
#  OR selecting 4 and 5 (4 + 5 = 9)
#  OR selecting 2 and 3 (2 + 3 = 5)
# Selecting elements 4 and 5 yields the maximum sum (4 + 5 = 9). Since the array is circular, the elements at index 0 (2) and index 4 (5) are considered adjacent.


# Example 2:
# Input: nums = [1, 2, 3, 1]
# Output: 4
# Explanation: Selecting elements 1 and 3 yields the maximum sum (1 + 3 = 4).

# Constraints:
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
'''

class Solution:
    def rob(self, nums: list[int]) -> int:
        """
        Calculates the maximum sum of non-adjacent elements in a circular array.

        Args:
            nums: The input circular array of integers.

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


        def house_robber(arr):  # Helper function for standard house robber problem (linear array)
            rob1, rob2 = 0, 0
            for num in arr:
                temp = max(num + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2

        # Consider two cases:
        # 1. Rob the first house, then we cannot rob the last house.
        # 2. Don't rob the first house, then we can rob the last house.
        return max(house_robber(nums[:-1]), house_robber(nums[1:]))


# Test cases
sol = Solution()
print(sol.rob([2, 4, 1, 3, 5]))  # Output: 9
print(sol.rob([1, 2, 3, 1]))  # Output: 4
print(sol.rob([1]))  # Output: 1
print(sol.rob([1, 2])) # Output: 2
print(sol.rob([2,7,9,3,1])) # Output: 11


'''
Time Complexity: O(N) - We iterate through the array twice in the house_robber function.
Space Complexity: O(1) - Constant extra space is used.
'''
```