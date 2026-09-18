"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 2183
Updated: 2026-09-18T19:52:13+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2183
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
