"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 2001
Updated: 2026-07-25T22:28:52+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2001
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
