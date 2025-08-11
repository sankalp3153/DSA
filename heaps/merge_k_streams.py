"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 823
Updated: 2025-08-11T17:47:41+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 823
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
