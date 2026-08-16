"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 2065
Updated: 2026-08-16T22:38:21+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2065
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
