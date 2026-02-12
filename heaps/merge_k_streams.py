"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 1467
Updated: 2026-02-12T15:51:18+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1467
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
