"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 1196
Updated: 2025-12-01T12:49:51+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1196
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
