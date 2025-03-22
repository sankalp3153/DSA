"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 343
Updated: 2025-03-22T18:43:39+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 343
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
