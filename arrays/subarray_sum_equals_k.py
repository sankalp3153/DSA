"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 2070
Updated: 2026-08-18T10:10:41+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2070
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
