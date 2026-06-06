"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 1835
Updated: 2026-06-06T13:25:33+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1835
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
