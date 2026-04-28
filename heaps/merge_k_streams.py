"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 1720
Updated: 2026-04-28T16:59:59+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1720
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
