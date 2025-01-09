"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 44
Updated: 2025-01-09T10:11:56+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 44
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
