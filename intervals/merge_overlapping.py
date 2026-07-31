"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 2022
Updated: 2026-07-31T20:11:33+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2022
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
