"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 432
Updated: 2025-04-17T15:08:39+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 432
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
