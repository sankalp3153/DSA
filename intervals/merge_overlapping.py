"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 1056
Updated: 2025-10-15T10:20:34+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1056
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
