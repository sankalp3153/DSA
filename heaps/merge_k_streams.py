"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 1743
Updated: 2026-05-06T11:30:17+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1743
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
