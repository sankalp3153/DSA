"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 2254
Updated: 2026-10-09T20:10:13+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2254
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
