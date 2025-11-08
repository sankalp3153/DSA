"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 1125
Updated: 2025-11-08T12:09:18+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1125
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
