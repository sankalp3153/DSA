"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 803
Updated: 2025-08-07T16:46:34+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 803
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
