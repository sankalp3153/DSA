"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 2111
Updated: 2026-08-26T15:36:05+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2111
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
