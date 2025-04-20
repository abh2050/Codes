```python
'''
# Sum of Even Numbers in a List

# Difficulty: Easy

# Problem Description:
# Given a list of integers, return the sum of all even numbers in the list.

# Examples:
# Example 1:
# Input: nums = [1, 2, 3, 4, 5]
# Output: 6
# Explanation: The even numbers in the list are 2 and 4. Their sum is 2 + 4 = 6.

# Example 2:
# Input: nums = [0, -2, 4, 6, 8]
# Output: 18
# Explanation: All numbers are even. Their sum is 0 + (-2) + 4 + 6 + 8 = 18.

# Example 3:
# Input: nums = [1, 3, 5, 7]
# Output: 0
# Explanation: There are no even numbers in the list.

# Constraints:
# 1 <= len(nums) <= 1000
# -1000 <= nums[i] <= 1000
'''

class Solution:
    def sumEvenNumbers(self, nums: list[int]) -> int:
        """
        Calculates the sum of even numbers in a list.

        Args:
            nums: A list of integers.

        Returns:
            The sum of all even numbers in the list.
        """
        sum_of_evens = 0
        for num in nums:
            if num % 2 == 0:
                sum_of_evens += num
        return sum_of_evens


# Time Complexity: O(n), where n is the length of the input list. We iterate through the list once.
# Space Complexity: O(1), as we only use a constant amount of extra space to store the sum.



# Test Cases
solution = Solution()

print(solution.sumEvenNumbers([1, 2, 3, 4, 5]))  # Output: 6
print(solution.sumEvenNumbers([0, -2, 4, 6, 8])) # Output: 18
print(solution.sumEvenNumbers([1, 3, 5, 7]))  # Output: 0
print(solution.sumEvenNumbers([]))  # Output: 0
print(solution.sumEvenNumbers([-2, -4, -6])) # Output: -12

```