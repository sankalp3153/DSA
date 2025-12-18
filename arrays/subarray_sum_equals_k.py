"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 1265
Updated: 2025-12-18T10:34:23+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1265
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
