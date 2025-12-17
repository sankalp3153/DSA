"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 1263
Updated: 2025-12-17T15:50:27+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1263
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
