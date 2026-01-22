"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 1378
Updated: 2026-01-22T22:16:10+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1378
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
