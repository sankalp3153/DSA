"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 688
Updated: 2025-07-01T14:02:23+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 688
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
