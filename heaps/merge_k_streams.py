"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 892
Updated: 2025-08-25T19:46:47+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 892
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
