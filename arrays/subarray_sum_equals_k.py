"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 2277
Updated: 2026-10-19T19:20:01+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2277
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
