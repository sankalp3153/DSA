"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 2045
Updated: 2026-08-07T18:09:35+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2045
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
