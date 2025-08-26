"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 895
Updated: 2025-08-26T15:34:50+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 895
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
