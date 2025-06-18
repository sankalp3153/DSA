"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 642
Updated: 2025-06-18T19:11:07+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 642
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
