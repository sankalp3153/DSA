"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 2295
Updated: 2026-10-27T17:31:55+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2295
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
