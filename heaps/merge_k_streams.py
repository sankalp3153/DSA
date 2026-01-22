"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 1375
Updated: 2026-01-22T18:14:01+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1375
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
