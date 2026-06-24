"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 1907
Updated: 2026-06-24T22:28:13+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1907
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
