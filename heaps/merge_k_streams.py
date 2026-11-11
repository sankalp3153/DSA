"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 2341
Updated: 2026-11-11T12:52:28+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2341
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
