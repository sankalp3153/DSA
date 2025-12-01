"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 1194
Updated: 2025-12-01T11:52:54+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1194
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
