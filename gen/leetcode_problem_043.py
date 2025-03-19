```python
'''
# Alternating Sum

# Difficulty: Easy

# Problem Description:
# Given a list of integers, return the alternating sum. The alternating sum is calculated by subtracting the even-indexed elements from the sum of the odd-indexed elements.

# Examples:
# Example 1:
# Input: nums = [1, 2, 3, 4, 5]
# Output: 3
# Explanation: (1 + 3 + 5) - (2 + 4) = 9 - 6 = 3

# Example 2:
# Input: nums = [0, 1]
# Output: 1
# Explanation: (1) - (0) = 1

# Example 3:
# Input: nums = []
# Output: 0


# Constraints:
# 0 <= nums.length <= 1000
# -1000 <= nums[i] <= 1000
'''

class Solution:
    def alternatingSum(self, nums: list[int]) -> int:
        """
        Calculates the alternating sum of a list of integers.

        Args:
            nums: A list of integers.

        Returns:
            The alternating sum.
        """
        odd_sum = 0
        even_sum = 0

        for i, num in enumerate(nums):
            if i % 2 == 0:  # Even index
                even_sum += num
            else:  # Odd index
                odd_sum += num
        
        return odd_sum - even_sum
        

# Time Complexity: O(n), where n is the length of the input list. We iterate through the list once.
# Space Complexity: O(1), as we only use a few variables to store the sums.



# Test Cases
solution = Solution()

print(solution.alternatingSum([1, 2, 3, 4, 5]))  # Output: 3
print(solution.alternatingSum([0, 1]))  # Output: 1
print(solution.alternatingSum([]))  # Output: 0
print(solution.alternatingSum([10, 20, 30, 40])) # Output: -20
print(solution.alternatingSum([-1, -2, -3])) # Output: 2
```