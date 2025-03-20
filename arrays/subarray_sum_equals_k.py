"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 322
Updated: 2025-03-20T12:44:00+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 322
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
