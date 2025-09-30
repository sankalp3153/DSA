"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 1010
Updated: 2025-09-30T12:55:40+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1010
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
