"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 1838
Updated: 2026-06-06T19:40:58+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1838
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
