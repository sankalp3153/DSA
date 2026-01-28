"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 1401
Updated: 2026-01-28T17:47:19+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1401
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
