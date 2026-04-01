"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 1631
Updated: 2026-04-01T13:44:25+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1631
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
