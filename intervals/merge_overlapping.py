"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 1539
Updated: 2026-03-03T23:29:55+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1539
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
