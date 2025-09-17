"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 964
Updated: 2025-09-17T22:13:59+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 964
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
