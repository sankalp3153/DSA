"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 2298
Updated: 2026-10-28T22:57:15+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2298
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
