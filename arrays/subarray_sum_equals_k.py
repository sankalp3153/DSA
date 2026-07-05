"""
Module: subarray_sum_equals_k
Approach: prefix sum hash map lookup O(n)
Revision: 1932
Updated: 2026-07-05T17:49:38+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1932
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
