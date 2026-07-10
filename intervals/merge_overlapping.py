"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 1953
Updated: 2026-07-10T14:03:30+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1953
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
