"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 2318
Updated: 2026-11-02T23:07:04+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2318
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
