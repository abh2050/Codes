```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular array of integers nums (nums[0] and nums[-1] are considered adjacent), find the maximum sum of a non-adjacent subsequence. 
# A non-adjacent subsequence is a subsequence where no two elements are adjacent in the circular array.

# Examples:
# Example 1:
# Input: nums = [2, 4, 1, 3, 5]
# Output: 10
# Explanation: Take elements [4, 5] and [2] for a total sum of 4 + 5 + 2 = 11.  Or [2, 3, 5] = 10. Or [4, 1, 5] = 10.  11 is the max.

# Example 2:
# Input: nums = [1, 2, 3, 1]
# Output: 4
# Explanation: Take elements [1, 3] for a sum of 4.

# Constraints:
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
'''

class Solution:
    def rob_circular(self, nums: list[int]) -> int:
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
        if n == 3:
            return max(nums)

        # Consider two cases:
        # 1. Include the first element, exclude the last
        # 2. Exclude the first element, include the last (potentially)

        def rob_linear(arr): # Helper function solves linear house robber problem (taken from LeetCode House Robber)
            prev_max, curr_max = 0, 0
            for num in arr:
                prev_max, curr_max = curr_max, max(curr_max, prev_max + num)
            return curr_max

        # Case 1: nums[0] included, nums[-1] excluded
        max1 = rob_linear(nums[:-1])  

        # Case 2: nums[0] excluded, nums[-1] possibly included
        max2 = rob_linear(nums[1:])

        return max(max1, max2)



    # Time Complexity: O(n) - We iterate through the array twice in rob_linear, once for each case.
    # Space Complexity: O(1) - We use constant extra space.



# Test Cases
solution = Solution()
print(solution.rob_circular([2, 4, 1, 3, 5]))  # Output: 11
print(solution.rob_circular([1, 2, 3, 1]))  # Output: 4
print(solution.rob_circular([1]))  # Output: 1
print(solution.rob_circular([1, 2]))  # Output: 2
print(solution.rob_circular([1, 2, 3]))  # Output: 3
print(solution.rob_circular([1,7,3,10,5])) # Output: 18

```