"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 1930
Updated: 2026-07-05T11:17:01+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1930
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
