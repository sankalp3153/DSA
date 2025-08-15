"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 846
Updated: 2025-08-15T18:40:32+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 846
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
