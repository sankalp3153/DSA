"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 1260
Updated: 2025-12-16T17:17:21+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1260
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
