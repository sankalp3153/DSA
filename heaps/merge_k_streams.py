"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 1766
Updated: 2026-05-17T20:31:20+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1766
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
