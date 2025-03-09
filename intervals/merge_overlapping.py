"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 274
Updated: 2025-03-09T18:48:59+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 274
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
