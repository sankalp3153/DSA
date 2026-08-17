"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 2068
Updated: 2026-08-17T16:32:29+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2068
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
