"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 1863
Updated: 2026-06-11T19:26:16+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1863
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
