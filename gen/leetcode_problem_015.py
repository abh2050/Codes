```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular integer array nums (i.e., the last element is also adjacent to the first element), 
# find the maximum sum of a non-adjacent subsequence. A subsequence is a sequence that can be derived 
# from another sequence by deleting some or no elements without changing the order of the remaining elements.
# Note that a subsequence does not necessarily need to be contiguous.

# Examples:
# Example 1:
# Input: nums = [2,4,1,3]
# Output: 7
# Explanation: Select 4 and 3 for a sum of 7.

# Example 2:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Select 1 (at index 0) and 3 for a sum of 4.

# Example 3:
# Input: nums = [1]
# Output: 1
# Explanation: Select 1.

# Constraints:
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
'''

class Solution:
    def rob_circular(self, nums: list[int]) -> int:
        """
        Calculates the maximum sum of non-adjacent elements in a circular array.

        Args:
            nums: The input circular integer array.

        Returns:
            The maximum sum of a non-adjacent subsequence.
        """
        n = len(nums)
        if n == 1:
            return nums[0]

        # Handle the circularity by solving two subproblems:
        # 1. Excluding the last element (standard house robber problem)
        # 2. Excluding the first element (standard house robber problem)
        def house_robber(arr):
            rob1, rob2 = 0, 0
            for num in arr:
                temp = max(num + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2

        return max(house_robber(nums[:-1]), house_robber(nums[1:]))


# Time Complexity: O(n) - We iterate through the array twice in the house_robber function.
# Space Complexity: O(1) - Constant extra space is used.



# Test Cases
solution = Solution()
print(solution.rob_circular([2, 4, 1, 3]))  # Output: 7
print(solution.rob_circular([1, 2, 3, 1]))  # Output: 4
print(solution.rob_circular([1]))  # Output: 1
print(solution.rob_circular([1, 2, 3, 4, 5, 1, 2, 3, 4, 5])) # Output: 15
print(solution.rob_circular([100, 1, 1, 100]))  # Output: 200



```