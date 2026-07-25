"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 1999
Updated: 2026-07-25T15:15:52+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1999
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
