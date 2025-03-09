"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 271
Updated: 2025-03-09T15:55:36+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 271
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
