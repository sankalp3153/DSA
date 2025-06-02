"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 573
Updated: 2025-06-02T11:43:49+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 573
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
