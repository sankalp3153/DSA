"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 110
Updated: 2025-01-28T16:52:06+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 110
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
