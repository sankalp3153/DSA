"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 205
Updated: 2025-02-18T19:42:49+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 205
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
