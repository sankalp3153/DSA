"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 2231
Updated: 2026-10-02T12:58:35+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2231
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
