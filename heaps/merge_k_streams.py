"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 1030
Updated: 2025-10-08T11:22:49+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1030
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
