"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 133
Updated: 2025-01-30T21:11:30+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 133
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
