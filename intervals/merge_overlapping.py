"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 1493
Updated: 2026-02-20T22:09:10+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1493
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
