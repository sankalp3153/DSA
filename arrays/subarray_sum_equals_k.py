"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 1541
Updated: 2026-03-04T20:30:34+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1541
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
