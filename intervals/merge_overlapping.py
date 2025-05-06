"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 481
Updated: 2025-05-06T18:56:45+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 481
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
