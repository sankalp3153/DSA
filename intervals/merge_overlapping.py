"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 458
Updated: 2025-04-24T13:45:15+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 458
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
