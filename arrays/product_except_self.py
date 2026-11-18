"""
Product of Array Except Self without division.
Time: O(n) | Space: O(1) auxiliary (excluding output array)
"""

from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    n = len(nums)
    result = [1] * n

    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result
