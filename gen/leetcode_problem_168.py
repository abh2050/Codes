```python
'''
# Maximum Sum of Non-Adjacent Elements in a Circular Array
# Difficulty: Medium

# Problem Description:
# Given a circular array of integers nums (where the last element is considered adjacent to the first element), 
# find the maximum sum of a subset of non-adjacent elements.

# Examples:
# Example 1:
# Input: nums = [2, 7, 9, 3, 1]
# Output: 11
# Explanation: Select the elements at indices 0, 2, and 4 (2 + 9 + 1 = 12).  Or select indices 1 and 3 (7+3 = 10) Or select 7 and 1 (8).  Or 2 and 9 (11) Or select only 9 etc.  Max is 11.

# Example 2:
# Input: nums = [1, 2, 3, 1]
# Output: 4
# Explanation: Select the elements at indices 0 and 2 (1 + 3 = 4).

# Constraints:
# 1 <= nums.length <= 2 * 10^4
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
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        # We consider two cases:
        # 1. Robbing the first house (means we cannot rob the last house)
        # 2. Not robbing the first house (means we can rob the last house)

        def house_robber(arr): # helper function for the standard house robber problem (non-circular)
            rob1, rob2 = 0, 0
            for num in arr:
                temp = max(rob1 + num, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        
        # Case 1: Include first element, exclude last
        max1 = house_robber(nums[:-1])

        # Case 2: Exclude first element, include last
        max2 = house_robber(nums[1:])
       
        return max(max1, max2)




# Test cases
solution = Solution()

print(solution.rob([2, 7, 9, 3, 1]))  # Output: 11
print(solution.rob([1, 2, 3, 1]))  # Output: 4
print(solution.rob([1])) # Output 1
print(solution.rob([1,2,1,1]))  # Output 3 (either 2 and 1 or 1 and 1)
print(solution.rob([]))  # Output 0



'''
Time Complexity: O(n), where n is the length of the input array. We iterate through the array twice in the worst case using our helper house robber function.

Space Complexity: O(1), as we use constant extra space. 
'''
```