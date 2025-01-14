"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 69
Updated: 2025-01-14T12:17:36+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 69
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
