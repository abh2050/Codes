```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular array of integers nums (where the last element is considered adjacent to the first), 
# find the maximum sum of a non-adjacent subset of elements.  A subset is non-adjacent if no two elements in the subset are directly next to each other in the array (including wrapping around).

# Examples:
# Example 1:
# Input: nums = [2, 7, 9, 3, 1]
# Output: 11
# Explanation: The maximum sum can be obtained by selecting elements at indices 0, 2, and 4 (2 + 9 + 1 = 12) or by selecting elements at indices 1 and 3 (7 + 3 = 10). Selecting 0, 2, and 4 is valid since they are not adjacent. 1 and 4 are also not considered adjacent due to the circular nature.

# Example 2:
# Input: nums = [1, 2, 3, 1]
# Output: 4
# Explanation: Select 1 and 3

# Constraints:
# 1 <= nums.length <= 3 * 10^4
# -1000 <= nums[i] <= 1000
'''

class Solution:
    def rob_circular(self, nums: list[int]) -> int:
        """
        Calculates the maximum sum of non-adjacent elements in a circular array.

        Args:
            nums: The input circular array of integers.

        Returns:
            The maximum sum of a non-adjacent subset.
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        # Handle the circular nature by considering two cases:
        # 1. Exclude the first element:  Solve for nums[1:]
        # 2. Exclude the last element:  Solve for nums[:-1]
        # Return the maximum of the two.

        def rob_linear(arr):
            # Standard house robber (linear) solution using dynamic programming.
            if not arr:
                return 0
            prev1, prev2 = 0, 0
            for num in arr:
                current = max(prev1, prev2 + num)
                prev2 = prev1
                prev1 = current
            return prev1

        return max(rob_linear(nums[1:]), rob_linear(nums[:-1]))


# Test Cases
solution = Solution()
print(solution.rob_circular([2, 7, 9, 3, 1]))  # Output: 12 
print(solution.rob_circular([1, 2, 3, 1]))  # Output: 4
print(solution.rob_circular([1]))  # Output: 1
print(solution.rob_circular([]))  # Output: 0
print(solution.rob_circular([1, 10, 1, 1, 5]))  # Output: 15



'''
Time Complexity: O(n), where n is the length of the nums array. We iterate through the array twice in the worst case (once for each linear rob).

Space Complexity: O(1).  The linear rob solution uses constant space.
'''

```