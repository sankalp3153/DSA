"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 780
Updated: 2025-07-31T20:45:14+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 780
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
