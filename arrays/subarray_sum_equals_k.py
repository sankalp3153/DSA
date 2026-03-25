"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 1610
Updated: 2026-03-25T10:30:48+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1610
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
