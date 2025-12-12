"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 1240
Updated: 2025-12-12T16:22:32+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1240
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
