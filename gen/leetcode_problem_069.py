```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular array of integers nums (where the last element is considered adjacent to the first element), 
# find the maximum sum of a non-adjacent subset of elements.  A non-adjacent subset means that no two selected 
# elements are directly next to each other in the array, including wrapping around (i.e., the first and last elements are considered adjacent).

# Examples:
# Example 1:
# Input: nums = [2, 7, 9, 3, 1]
# Output: 11
# Explanation: Choose elements at index 0, 2, and 4 (2 + 9 + 1 = 11).

# Example 2:
# Input: nums = [1, 2, 3, 1]
# Output: 4
# Explanation: Choose elements at index 0 and 2 (1 + 3 = 4).

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
        
        # Consider two scenarios:
        # 1. Exclude the last element:  Calculate max sum for nums[:-1]
        # 2. Exclude the first element: Calculate max sum for nums[1:]
        # Return the maximum of the two scenarios

        def house_robber(arr):
            """Helper function to calculate max sum of non-adjacent elements in a linear array (House Robber I)."""
            rob1, rob2 = 0, 0
            for num in arr:
                temp = max(num + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2

        return max(house_robber(nums[:-1]), house_robber(nums[1:]))
    


# Test Cases
solution = Solution()

print(solution.rob([2, 7, 9, 3, 1]))  # Output: 11
print(solution.rob([1, 2, 3, 1]))  # Output: 4
print(solution.rob([1]))  # Output: 1
print(solution.rob([1, 3, 1, 3, 100])) # Output: 103
print(solution.rob([1, 2, 3])) # Output: 4


'''
Time Complexity: O(N), where N is the length of the input array. We iterate through the array twice in the worst case 
                  (once for each subproblem).

Space Complexity: O(1). We use a constant amount of extra space.
'''

```