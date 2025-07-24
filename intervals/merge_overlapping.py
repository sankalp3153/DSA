"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 757
Updated: 2025-07-24T20:00:09+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 757
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
