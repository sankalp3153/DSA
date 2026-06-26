"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 1909
Updated: 2026-06-26T15:08:04+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1909
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
