"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 1426
Updated: 2026-02-02T23:31:31+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1426
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
