"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 90
Updated: 2025-01-23T10:08:40+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 90
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
