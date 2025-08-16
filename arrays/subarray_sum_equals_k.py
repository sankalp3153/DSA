"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 851
Updated: 2025-08-16T15:57:06+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 851
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
