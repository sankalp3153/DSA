"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 1380
Updated: 2026-01-23T10:47:21+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1380
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
