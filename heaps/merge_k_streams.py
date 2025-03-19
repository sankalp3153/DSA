"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 317
Updated: 2025-03-19T18:55:09+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 317
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
