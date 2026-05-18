"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 1769
Updated: 2026-05-18T12:25:12+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1769
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
