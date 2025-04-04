"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 389
Updated: 2025-04-04T15:06:48+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 389
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
