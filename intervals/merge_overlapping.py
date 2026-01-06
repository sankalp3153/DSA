"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 1332
Updated: 2026-01-06T14:11:20+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1332
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
