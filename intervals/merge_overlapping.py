"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 711
Updated: 2025-07-13T18:51:05+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 711
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
