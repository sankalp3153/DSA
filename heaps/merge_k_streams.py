"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 2157
Updated: 2026-09-04T23:30:06+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2157
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
