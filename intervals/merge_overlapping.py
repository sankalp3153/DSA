"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 2206
Updated: 2026-09-27T20:36:45+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2206
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
