"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 1329
Updated: 2026-01-05T12:35:48+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1329
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
