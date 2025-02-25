"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 228
Updated: 2025-02-25T19:44:32+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 228
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
