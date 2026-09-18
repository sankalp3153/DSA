"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 2180
Updated: 2026-09-18T10:52:02+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2180
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
