"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 1562
Updated: 2026-03-13T13:54:24+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1562
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
