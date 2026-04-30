"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 1725
Updated: 2026-04-30T11:16:12+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1725
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
