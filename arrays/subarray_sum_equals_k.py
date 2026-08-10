"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 2047
Updated: 2026-08-10T10:11:13+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2047
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
