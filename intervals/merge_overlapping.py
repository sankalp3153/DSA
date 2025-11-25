"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 1171
Updated: 2025-11-25T22:48:05+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1171
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
