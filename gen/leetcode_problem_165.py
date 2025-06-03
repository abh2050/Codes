```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular array of integers nums (meaning the last element is considered adjacent to the first element), 
# find the maximum sum of a non-adjacent subset of elements.  A subset is "non-adjacent" if no two elements in the subset are adjacent in the circular array.

# Examples:
# Example 1:
# Input: nums = [2, 7, 9, 3, 1]
# Output: 11
# Explanation: Pick nums[0] (2), nums[2] (9), and nums[4] (1). The sum is 11.

# Example 2:
# Input: nums = [1, 2, 3, 1]
# Output: 4
# Explanation: Pick nums[0] (1) and nums[2] (3). The sum is 4.

# Constraints:
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^4
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
        if n == 0: return 0
        if n == 1: return nums[0]
        if n == 2: return max(nums)


        # Consider two cases:
        # 1. Include the first element (exclude the last)
        # 2. Exclude the first element (can include the last)

        # Helper function to calculate max sum for a linear array (house robber problem)
        def rob_linear(arr):
            prev_max, curr_max = 0, 0
            for num in arr:
                temp = curr_max
                curr_max = max(prev_max + num, curr_max)
                prev_max = temp
            return curr_max
        
        # Case 1: Include first, exclude last
        include_first = rob_linear(nums[:-1])

        # Case 2: Exclude first, can include last
        exclude_first = rob_linear(nums[1:])

        return max(include_first, exclude_first)



# Test cases
solution = Solution()

print(solution.rob_circular([2, 7, 9, 3, 1]))  # Output: 11
print(solution.rob_circular([1, 2, 3, 1]))  # Output: 4
print(solution.rob_circular([1])) # Output: 1
print(solution.rob_circular([1,2])) # Output: 2
print(solution.rob_circular([1,5,2,1,3])) # Output: 8
print(solution.rob_circular([1,3,1,3,100]))  # Output 103


'''
Time Complexity: O(n) - We iterate through the array twice in the rob_linear function.
Space Complexity: O(1) - We use constant extra space.
'''

```