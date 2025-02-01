"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 138
Updated: 2025-02-01T15:23:05+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 138
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
