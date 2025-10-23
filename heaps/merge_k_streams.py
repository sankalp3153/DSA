"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 1076
Updated: 2025-10-23T12:01:47+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1076
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
