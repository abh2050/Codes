def maximize_odd_subarray_sum(nums, k):
    """
    Finds the maximum sum of consecutive odd number subarrays of length k.

    Args:
        nums: A list of integers.
        k: The length of the subarray.

    Returns:
        The maximum sum of all possible consecutive odd number subarrays of length k, or 0 if no such subarray exists.
    """

    max_sum = 0
    for i in range(len(nums) - k + 1):
        subarray = nums[i:i+k]
        is_all_odd = all(num % 2 != 0 for num in subarray)  # Check if all elements are odd

        if is_all_odd:
            current_sum = sum(subarray)
            max_sum = max(max_sum, current_sum)

    return max_sum
