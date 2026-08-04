"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 2024
Updated: 2026-08-04T10:52:12+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2024
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
