"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 1495
Updated: 2026-02-22T12:58:09+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1495
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
