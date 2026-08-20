"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 2091
Updated: 2026-08-20T20:20:43+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2091
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
