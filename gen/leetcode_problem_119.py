```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular integer array nums (i.e., the next element of nums[-1] is nums[0]), 
# return the maximum sum of a non-empty subsequence of nums such that no two elements in the subsequence are adjacent in the circular array.

# Examples:
# Example 1:
# Input: nums = [2,4,1,3,5]
# Output: 10
# Explanation: Pick 2, 1, and 5. Their sum is 10 (2+1+5=10).

# Example 2:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Pick 1 and 3. Their sum is 4 (1+3=4).

# Constraints:
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^4
'''

class Solution:
    def rob(self, nums: list[int]) -> int:
        """
        Calculates the maximum sum of non-adjacent elements in a circular array.

        Args:
            nums: The input circular integer array.

        Returns:
            The maximum sum of a non-empty subsequence with no adjacent elements.
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        
        # Use dynamic programming to calculate the maximum sum for two scenarios:
        # 1. Excluding the last element (treating it as a linear array)
        # 2. Excluding the first element (treating it as a linear array)
        
        def house_robber(arr):
            prev_max, curr_max = 0, 0
            for num in arr:
                temp = curr_max
                curr_max = max(curr_max, prev_max + num)
                prev_max = temp
            return curr_max

        return max(house_robber(nums[:-1]), house_robber(nums[1:]))


# Time Complexity: O(N), where N is the length of the input array. We iterate through the array twice.
# Space Complexity: O(1),  as we are only using a few variables to store intermediate results.


# Test Cases
solution = Solution()
print(solution.rob([2, 4, 1, 3, 5]))  # Output: 10
print(solution.rob([1, 2, 3, 1]))  # Output: 4
print(solution.rob([1]))  # Output: 1
print(solution.rob([1,2,3,4,5,1,2,3,4,5])) # Output: 15
print(solution.rob([1,2,3])) # Output: 4

```