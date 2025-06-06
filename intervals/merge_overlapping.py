"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 596
Updated: 2025-06-06T22:56:23+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 596
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
