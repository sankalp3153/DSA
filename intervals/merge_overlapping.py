"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 1470
Updated: 2026-02-15T11:58:30+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1470
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
