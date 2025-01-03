"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 18
Updated: 2025-01-03T22:48:10+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 18
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
