"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 87
Updated: 2025-01-22T23:23:46+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 87
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
