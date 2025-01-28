"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 113
Updated: 2025-01-28T20:13:19+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 113
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
