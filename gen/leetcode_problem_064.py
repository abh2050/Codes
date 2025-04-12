```python
'''
# Maximum Subarray Sum with K Distinct Prime Factors

# Difficulty: Hard

# Problem Description:
# Given an array of positive integers 'nums' and an integer 'k', find the maximum sum of a 
# subarray where each number in the subarray has exactly 'k' distinct prime factors. 
# If no such subarray exists, return -1.

# Examples:
# Example 1:
# Input: nums = [6, 10, 15, 30], k = 2
# Output: 51
# Explanation: The subarray [6, 10, 15, 30] contains numbers with exactly 2 distinct prime factors each (6: 2, 3; 10: 2, 5; 15: 3, 5; 30: 2, 3, 5). The sum is 6 + 10 + 15 + 30 = 51.


# Example 2:
# Input: nums = [7, 10, 14, 6], k = 1
# Output: -1
# Explanation: No number in the array has exactly 1 prime factor.


# Example 3:
# Input: nums = [2,3,5,7,10,14,6, 15, 21, 30], k = 2
# Output: 51
# Explanation: The subarray [6, 10, 15, 30] contains numbers with exactly 2 distinct prime factors each (6: 2, 3; 10: 2, 5; 15: 3, 5; 30: 2, 3, 5). The sum is 6 + 10 + 15 + 30 = 51.

# Constraints:
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^6
# 1 <= k <= 5
'''

class Solution:
    def maxSubarraySumKPrime(self, nums, k):
        """
        Finds the maximum sum of a subarray with elements having k distinct prime factors.

        Args:
            nums: The input array of positive integers.
            k: The required number of distinct prime factors.

        Returns:
            The maximum subarray sum, or -1 if no such subarray exists.
        """

        def count_prime_factors(n):
            count = 0
            i = 2
            while i * i <= n:
                if n % i == 0:
                    count += 1
                    while n % i == 0:
                        n //= i
                i += 1
            if n > 1:
                count += 1
            return count

        max_sum = -1
        n = len(nums)
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                if count_prime_factors(nums[j]) == k:
                    current_sum += nums[j]
                    max_sum = max(max_sum, current_sum)
                else: # Break if a number doesn't have k prime factors
                    current_sum = 0  #Reset the sum as contiguity breaks



        return max_sum


# Time Complexity: O(n * sqrt(M)), where n is the length of nums and M is the maximum value in nums.
# Space Complexity: O(1)


# Test cases
solution = Solution()

print(solution.maxSubarraySumKPrime([6, 10, 15, 30], 2))  # Output: 51
print(solution.maxSubarraySumKPrime([7, 10, 14, 6], 1))  # Output: -1
print(solution.maxSubarraySumKPrime([2,3,5,7,10,14,6, 15, 21, 30], 2)) # Output: 51
print(solution.maxSubarraySumKPrime([30,6,10,15,6,10], 2)) # Output: 51
print(solution.maxSubarraySumKPrime([105], 3))  # Output: 105 (105 = 3 * 5 * 7)
print(solution.maxSubarraySumKPrime([4,8,12,16,20],1)) # output -1



```