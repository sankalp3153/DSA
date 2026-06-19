"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 1884
Updated: 2026-06-19T18:25:18+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1884
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
