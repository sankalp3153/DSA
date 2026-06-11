"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 1861
Updated: 2026-06-11T15:32:17+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1861
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
