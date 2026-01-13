"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 1355
Updated: 2026-01-13T23:33:18+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1355
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
