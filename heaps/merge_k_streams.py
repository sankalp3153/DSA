"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 1145
Updated: 2025-11-19T10:46:46+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1145
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
