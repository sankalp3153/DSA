"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 1102
Updated: 2025-10-31T14:06:17+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1102
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
