"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 412
Updated: 2025-04-11T14:03:36+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 412
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
