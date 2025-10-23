"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 1079
Updated: 2025-10-23T19:26:29+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1079
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
