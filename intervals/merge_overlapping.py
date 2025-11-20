"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 1148
Updated: 2025-11-20T10:22:17+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1148
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
