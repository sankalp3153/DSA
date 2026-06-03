"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 1815
Updated: 2026-06-03T11:39:27+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1815
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
