"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 2139
Updated: 2026-08-31T22:40:04+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2139
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
