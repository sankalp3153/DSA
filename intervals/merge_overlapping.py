"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 734
Updated: 2025-07-19T15:18:20+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 734
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
