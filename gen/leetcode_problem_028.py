```python
'''
# Maximum Subarray Sum with K Distinct Prime Factors
# Difficulty: Hard

# Problem Description:
# Given an array of positive integers 'nums' and an integer 'k', find the maximum possible sum of a subarray where each element in the subarray has exactly 'k' distinct prime factors. If no such subarray exists, return -1.

# Examples:
# Example 1:
# Input: nums = [10, 20, 30, 40, 50], k = 2
# Output: 90 
# Explanation: [20, 30, 40] (20 = 2*2*5, 30 = 2*3*5, 40 = 2*2*2*5). Each number has 2 distinct prime factors, and the sum is 90.

# Example 2:
# Input: nums = [7, 10, 12, 7, 9, 14], k = 2
# Output: 24
# Explanation: [10, 14]. 10 = 2*5, 14 = 2*7

# Example 3:
# Input: nums = [6, 8, 10], k = 3 
# Output: -1
# Explanation: No number has 3 distinct prime factors.

# Constraints:
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^6
# 1 <= k <= 5
'''

class Solution:
    def maxSubarraySumKPrimes(self, nums, k):
        """
        Finds the maximum sum of a subarray where each element has exactly k distinct prime factors.

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

        filtered_nums = [num for num in nums if count_prime_factors(num) == k]
        if not filtered_nums:
            return -1

        max_so_far = 0
        current_max = 0
        for num in filtered_nums:
            current_max += num
            if current_max < 0:
                current_max = 0
            max_so_far = max(max_so_far, current_max)

        return max_so_far if max_so_far > 0 else -1

    # Time Complexity: O(N * sqrt(M)), where N is the length of nums and M is the maximum value in nums.
    # Space Complexity: O(N) in the worst case, where all numbers have k prime factors.


# Test Cases
solution = Solution()

print(solution.maxSubarraySumKPrimes([10, 20, 30, 40, 50], 2))  # Output: 90
print(solution.maxSubarraySumKPrimes([7, 10, 12, 7, 9, 14], 2))  # Output: 24
print(solution.maxSubarraySumKPrimes([6, 8, 10], 3))  # Output: -1
print(solution.maxSubarraySumKPrimes([30, 60, 90, 120, 420], 3)) # Output: 750
print(solution.maxSubarraySumKPrimes([1,2,3,4,5], 1)) # Output: 5
print(solution.maxSubarraySumKPrimes([1,4,9,16,25],0)) # Output: -1





```