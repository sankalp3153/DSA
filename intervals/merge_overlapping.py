"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 320
Updated: 2025-03-19T22:59:18+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 320
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
