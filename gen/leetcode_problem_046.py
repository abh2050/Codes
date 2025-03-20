```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular array of integers nums (meaning the last element is considered adjacent to the first), 
# find the maximum sum of a subset of its elements such that no two adjacent elements in the circular array are selected.

# Examples:
# Example 1:
# Input: nums = [2, 1, 4, 9]
# Output: 11
# Explanation: The optimal subset is {2, 9}, which has a sum of 11.

# Example 2:
# Input: nums = [1, 2, 3, 1]
# Output: 4
# Explanation: The optimal subset is {1, 3}, which has a sum of 4.

# Example 3:
# Input: nums = [1]
# Output: 1

# Constraints:
# 1 <= nums.length <= 3 * 10^4
# -10^4 <= nums[i] <= 10^4
'''

class Solution:
    def rob(self, nums: list[int]) -> int:
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
        
        # We consider two cases:
        # 1. Robbing the first house (excluding the last)
        # 2. Robbing the last house (excluding the first)
        # The maximum of these two scenarios will be the final answer.
        return max(self.house_robber_linear(nums[:-1]), self.house_robber_linear(nums[1:]))

    def house_robber_linear(self, nums: list[int]) -> int:
        """
        Helper function to solve the classic House Robber problem on a linear array.
        Uses dynamic programming with O(1) space.
        """
        n = len(nums)
        rob1, rob2 = 0, 0

        for i in range(n):
            temp = max(nums[i] + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2



# Test Cases
solution = Solution()
print(solution.rob([2, 1, 4, 9]))  # Output: 11
print(solution.rob([1, 2, 3, 1]))  # Output: 4
print(solution.rob([1]))          # Output: 1
print(solution.rob([1, 3, 1, 3, 100]))  # Output: 103


'''
Time Complexity: O(N), where N is the length of the input array. We iterate through the array twice in the worst case.

Space Complexity: O(1), as we use constant extra space for the dynamic programming approach.
'''

```