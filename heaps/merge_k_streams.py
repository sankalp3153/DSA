"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 2226
Updated: 2026-10-01T12:30:12+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2226
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
