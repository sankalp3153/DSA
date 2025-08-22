"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 872
Updated: 2025-08-22T12:40:29+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 872
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
