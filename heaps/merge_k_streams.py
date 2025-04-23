"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 455
Updated: 2025-04-23T16:00:11+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 455
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
