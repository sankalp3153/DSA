"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 182
Updated: 2025-02-12T22:31:07+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 182
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
