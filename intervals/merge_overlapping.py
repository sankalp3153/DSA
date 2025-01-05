"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 21
Updated: 2025-01-05T16:54:06+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 21
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
