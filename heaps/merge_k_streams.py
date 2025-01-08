"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 41
Updated: 2025-01-08T19:55:45+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 41
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
