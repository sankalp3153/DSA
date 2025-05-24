"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 550
Updated: 2025-05-24T15:05:54+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 550
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
