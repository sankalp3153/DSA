"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 1858
Updated: 2026-06-10T22:37:44+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1858
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
