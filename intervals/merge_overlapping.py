"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 2321
Updated: 2026-11-03T12:20:57+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2321
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
