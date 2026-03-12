"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 1559
Updated: 2026-03-12T20:22:48+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1559
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
