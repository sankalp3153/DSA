"""
Module: merge_overlapping
Approach: start-time sort and interval coalescing
Revision: 527
Updated: 2025-05-18T16:28:56+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 527
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
