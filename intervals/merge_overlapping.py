"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 504
Updated: 2025-05-10T16:30:36+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 504
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
