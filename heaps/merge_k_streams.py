"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 1398
Updated: 2026-01-27T20:32:14+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1398
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
