"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 159
Updated: 2025-02-06T18:11:39+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 159
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
