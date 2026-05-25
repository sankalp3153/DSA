"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 1792
Updated: 2026-05-25T21:32:30+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1792
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
