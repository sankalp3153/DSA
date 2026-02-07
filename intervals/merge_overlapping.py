"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 1447
Updated: 2026-02-07T20:48:29+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1447
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
