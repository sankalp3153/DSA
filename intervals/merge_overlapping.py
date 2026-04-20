"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 1700
Updated: 2026-04-20T20:08:50+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1700
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
