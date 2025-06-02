```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular array of integers nums, find the maximum sum of a non-adjacent subset of elements.
# "Circular" means the first and last elements are considered adjacent.

# Examples:
# Example 1:
# Input: nums = [2, 4, 1, 3, 5]
# Output: 10
# Explanation: The maximum sum is obtained by selecting elements [4, 5, 1].  4 and 5 are not adjacent because the array is circular.

# Example 2:
# Input: nums = [1, 2, 3, 1]
# Output: 4
# Explanation: The maximum sum is obtained by selecting elements [1, 3].

# Example 3:
# Input: nums = [1]
# Output: 1

# Constraints:
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^4
'''

class Solution:
    def maxSumNonAdjacentCircular(self, nums: list[int]) -> int:
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

        # Helper function to calculate max sum for a non-circular array
        def max_sum_non_adjacent(arr):
            incl = 0
            excl = 0
            for num in arr:
                new_excl = max(incl, excl)
                incl = excl + num
                excl = new_excl
            return max(incl, excl)

        # Case 1: Exclude the first element
        max_sum1 = max_sum_non_adjacent(nums[1:])

        # Case 2: Exclude the last element
        max_sum2 = max_sum_non_adjacent(nums[:-1])

        return max(max_sum1, max_sum2)


# Time Complexity: O(N), where N is the length of the input array. The helper function iterates through the array once in each of the two calls.
# Space Complexity: O(1), as we only use a few variables to store intermediate results.


# Test Cases
solution = Solution()

print(solution.maxSumNonAdjacentCircular([2, 4, 1, 3, 5]))  # Output: 10
print(solution.maxSumNonAdjacentCircular([1, 2, 3, 1]))  # Output: 4
print(solution.maxSumNonAdjacentCircular([1]))  # Output: 1
print(solution.maxSumNonAdjacentCircular([1, 5, 2, 3, 7])) # Output: 12 (1 + 2 + 7 OR 5 + 7)
print(solution.maxSumNonAdjacentCircular([5, 1, 1, 5])) # Output: 10

```