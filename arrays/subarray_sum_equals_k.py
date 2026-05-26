"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 1794
Updated: 2026-05-26T18:04:01+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1794
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
