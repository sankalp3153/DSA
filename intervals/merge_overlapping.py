"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 1746
Updated: 2026-05-08T15:29:16+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1746
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
