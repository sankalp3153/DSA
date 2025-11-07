"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 1122
Updated: 2025-11-07T16:38:16+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1122
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
