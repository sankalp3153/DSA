"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 1996
Updated: 2026-07-24T18:36:28+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1996
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
