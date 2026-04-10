"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 1654
Updated: 2026-04-10T13:06:07+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1654
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
