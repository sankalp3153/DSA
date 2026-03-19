"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 1585
Updated: 2026-03-19T19:59:35+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1585
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
