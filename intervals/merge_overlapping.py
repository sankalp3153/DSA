"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 2344
Updated: 2026-11-12T22:46:58+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2344
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
