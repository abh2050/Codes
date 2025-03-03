from collections import defaultdict

class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        """
        Finds the number of subarrays with exactly k distinct integers.

        Args:
            nums: The input array of integers.
            k: The desired number of distinct integers in the subarrays.

        Returns:
            The number of subarrays with exactly k distinct integers.
        """

        def atMostK(nums, k):
            """
            Helper function to find the number of subarrays with at most k distinct integers.
            """
            left = 0
            count = 0
            freq = defaultdict(int)
            distinct = 0

            for right in range(len(nums)):
                freq[nums[right]] += 1
                if freq[nums[right]] == 1:
                    distinct += 1

                while distinct > k:
                    freq[nums[left]] -= 1
                    if freq[nums[left]] == 0:
                        distinct -= 1
                    left += 1

                count += (right - left + 1)

            return count

        return atMostK(nums, k) - atMostK(nums, k - 1)
