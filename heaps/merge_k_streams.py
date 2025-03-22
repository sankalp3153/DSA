"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 340
Updated: 2025-03-22T12:05:15+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 340
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
