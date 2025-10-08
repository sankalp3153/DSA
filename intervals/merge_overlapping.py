"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 1033
Updated: 2025-10-08T17:59:04+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1033
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
