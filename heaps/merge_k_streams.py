"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 1168
Updated: 2025-11-25T11:31:50+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1168
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
