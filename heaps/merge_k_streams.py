"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 1950
Updated: 2026-07-09T18:42:10+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1950
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
