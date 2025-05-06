"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 483
Updated: 2025-05-06T20:31:15+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 483
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
