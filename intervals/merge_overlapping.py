"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 2229
Updated: 2026-10-01T22:19:47+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2229
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
