"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 1283
Updated: 2025-12-23T23:05:36+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1283
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
