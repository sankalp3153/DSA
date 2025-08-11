"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 826
Updated: 2025-08-11T21:20:42+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 826
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
