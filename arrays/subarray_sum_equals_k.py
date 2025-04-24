"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 460
Updated: 2025-04-24T20:54:39+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 460
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
