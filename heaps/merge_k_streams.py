"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 685
Updated: 2025-06-28T20:37:30+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 685
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
