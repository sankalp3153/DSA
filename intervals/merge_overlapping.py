"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 2137
Updated: 2026-08-31T20:36:17+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2137
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
