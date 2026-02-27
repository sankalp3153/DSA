"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 1516
Updated: 2026-02-27T18:29:13+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1516
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
