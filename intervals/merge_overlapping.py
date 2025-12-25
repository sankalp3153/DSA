"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 1286
Updated: 2025-12-25T14:03:47+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1286
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
