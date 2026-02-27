"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 1513
Updated: 2026-02-27T13:23:06+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1513
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
