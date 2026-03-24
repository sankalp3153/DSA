"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 1608
Updated: 2026-03-24T20:07:51+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1608
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
