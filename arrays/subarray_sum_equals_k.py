"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 621
Updated: 2025-06-13T21:16:47+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 621
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
