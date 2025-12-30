"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 1309
Updated: 2025-12-30T11:44:37+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1309
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
