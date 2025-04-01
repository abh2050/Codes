```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular integer array nums, return the maximum possible sum of a non-empty subarray of nums, where non-adjacent elements are chosen.
# A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n], where n is the length of nums.

# Examples:
# Example 1:
# Input: nums = [2,7,9,3,1]
# Output: 11
# Explanation: Choose nums[0] = 2, nums[2] = 9 and nums[4] = 1. The sum is 2 + 9 + 1 = 11.

# Example 2:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Choose nums[0] = 1 and nums[2] = 3. The sum is 1 + 3 = 4.

# Constraints:
# 1 <= nums.length <= 4 * 10^4
# -10^4 <= nums[i] <= 10^4
'''

class Solution:
    def rob(self, nums: list[int]) -> int:
        """
        Calculates the maximum sum of non-adjacent elements in a circular array.

        Args:
            nums: The input circular integer array.

        Returns:
            The maximum possible sum of a non-empty subarray.
        """
        n = len(nums)
        if n == 1:
            return nums[0]

        # Consider two scenarios:
        # 1. Rob the first house, but not the last.
        # 2. Don't rob the first house, but potentially rob the last.

        def house_robber(arr):
            rob1, rob2 = 0, 0
            for num in arr:
                temp = max(num + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2

        # Scenario 1: Exclude the last element
        max1 = house_robber(nums[:-1])

        # Scenario 2: Exclude the first element
        max2 = house_robber(nums[1:])

        return max(max1, max2)

# Time Complexity: O(n) - We iterate through the array twice in the house_robber function.
# Space Complexity: O(1) - We use constant extra space.



# Test Cases
solution = Solution()
print(solution.rob([2, 7, 9, 3, 1]))  # Output: 11
print(solution.rob([1, 2, 3, 1]))  # Output: 4
print(solution.rob([1]))  # Output: 1
print(solution.rob([1, 2])) # Output: 2
print(solution.rob([1,3,1,3,100])) # Output: 103

```