"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 2134
Updated: 2026-08-31T12:20:54+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2134
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
