"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 1352
Updated: 2026-01-13T12:01:23+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1352
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
