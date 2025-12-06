"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 1217
Updated: 2025-12-06T14:44:46+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1217
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
