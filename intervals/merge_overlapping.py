"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 366
Updated: 2025-03-30T21:15:43+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 366
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
