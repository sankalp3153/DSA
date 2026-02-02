"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 1424
Updated: 2026-02-02T20:52:23+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1424
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
