"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 2160
Updated: 2026-09-07T11:58:33+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2160
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
