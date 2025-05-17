"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 524
Updated: 2025-05-17T14:22:16+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 524
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
