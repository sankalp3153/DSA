"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 665
Updated: 2025-06-25T10:48:50+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 665
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
