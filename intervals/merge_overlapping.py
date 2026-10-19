"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 2275
Updated: 2026-10-19T15:13:56+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2275
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
