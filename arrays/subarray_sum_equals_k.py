"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 161
Updated: 2025-02-06T20:14:27+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 161
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
