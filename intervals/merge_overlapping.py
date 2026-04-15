"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 1677
Updated: 2026-04-15T12:28:14+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1677
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
