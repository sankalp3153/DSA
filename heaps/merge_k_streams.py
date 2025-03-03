"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 248
Updated: 2025-03-03T15:00:10+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 248
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
