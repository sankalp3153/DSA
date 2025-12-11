"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 1237
Updated: 2025-12-11T22:29:45+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1237
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
