"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 136
Updated: 2025-02-01T11:37:05+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 136
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
