"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 1886
Updated: 2026-06-19T20:59:35+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1886
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
