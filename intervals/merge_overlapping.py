"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 67
Updated: 2025-01-13T14:10:37+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 67
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
