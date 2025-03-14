"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 297
Updated: 2025-03-14T13:40:53+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 297
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
