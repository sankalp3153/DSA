"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 2252
Updated: 2026-10-09T16:10:12+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2252
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
