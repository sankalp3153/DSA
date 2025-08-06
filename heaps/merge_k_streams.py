"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 800
Updated: 2025-08-06T23:23:07+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 800
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
