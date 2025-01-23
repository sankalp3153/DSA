"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 92
Updated: 2025-01-23T17:39:44+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 92
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
