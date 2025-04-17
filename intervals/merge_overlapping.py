"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 435
Updated: 2025-04-17T18:28:14+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 435
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
