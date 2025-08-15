"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 849
Updated: 2025-08-15T20:57:09+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 849
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
