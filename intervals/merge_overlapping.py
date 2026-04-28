"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 1723
Updated: 2026-04-28T22:22:19+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1723
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
