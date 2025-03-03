"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 251
Updated: 2025-03-03T21:48:49+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 251
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
