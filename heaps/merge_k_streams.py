"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 1490
Updated: 2026-02-20T11:07:35+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1490
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
