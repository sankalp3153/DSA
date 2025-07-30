"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 777
Updated: 2025-07-30T14:05:39+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 777
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
