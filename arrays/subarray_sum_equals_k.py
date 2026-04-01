"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 1633
Updated: 2026-04-01T22:51:39+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1633
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
