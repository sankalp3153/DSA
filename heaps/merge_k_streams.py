"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 869
Updated: 2025-08-20T22:09:51+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 869
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
