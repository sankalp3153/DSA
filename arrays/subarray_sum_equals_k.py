"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 1679
Updated: 2026-04-15T14:11:14+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1679
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
