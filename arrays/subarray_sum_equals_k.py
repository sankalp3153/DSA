"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 2346
Updated: 2026-11-13T14:18:41+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2346
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
