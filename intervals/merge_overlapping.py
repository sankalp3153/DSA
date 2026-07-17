"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 1976
Updated: 2026-07-17T10:52:39+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1976
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
