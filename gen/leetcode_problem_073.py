```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular array of integers nums (meaning the last element is considered adjacent to the first), 
# find the maximum sum of a subset of its elements where no two adjacent elements in the circular array are chosen.

# Examples:
# Example 1:
# Input: nums = [2, 7, 9, 3, 1]
# Output: 11
# Explanation: Choose elements at indices 0, 2, and 4.  2 + 9 + 1 = 12. Or choose indices 1 and 3. 7 + 3 = 10. The max is 11 using indices 1 and 4 (7+1) or 0 and 2 (2+9).

# Example 2:
# Input: nums = [1, 2, 3, 1]
# Output: 4
# Explanation: Choose elements at indices 0 and 2. 1 + 3 = 4.

# Constraints:
# 1 <= nums.length <= 3 * 10^4
# -10^4 <= nums[i] <= 10^4
'''

class Solution:
    def rob_circular(self, nums: list[int]) -> int:
        """
        Calculates the maximum sum of non-adjacent elements in a circular array.

        Args:
            nums: The input circular array of integers.

        Returns:
            The maximum sum of non-adjacent elements.
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)

        # Consider two scenarios:
        # 1. Include the first element, exclude the last
        # 2. Exclude the first element, include the last

        def house_robber(arr):  # Standard house robber problem (linear array)
            prev_max, curr_max = 0, 0
            for num in arr:
                temp = curr_max
                curr_max = max(curr_max, prev_max + num)
                prev_max = temp
            return curr_max
        
        # Scenario 1: Exclude last element
        max1 = house_robber(nums[:-1])

        # Scenario 2: Exclude first element
        max2 = house_robber(nums[1:])

        return max(max1, max2)


# Test Cases
solution = Solution()

print(solution.rob_circular([2, 7, 9, 3, 1]))  # Output: 11 or 12 depending on which indices chosen
print(solution.rob_circular([1, 2, 3, 1]))  # Output: 4
print(solution.rob_circular([1, 2, 3])) # Output 4 (choose 1 and 3)
print(solution.rob_circular([1])) # Output 1
print(solution.rob_circular([])) # Output 0
print(solution.rob_circular([1,3,1,3,100])) # Output 103


'''
Time Complexity: O(N) - We iterate through the array twice in the `house_robber` function.
Space Complexity: O(1) - We use constant extra space.
'''

```