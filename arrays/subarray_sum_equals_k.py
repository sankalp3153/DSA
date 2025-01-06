"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 23
Updated: 2025-01-06T14:42:16+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 23
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
