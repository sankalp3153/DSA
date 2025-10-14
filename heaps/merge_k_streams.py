"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 1053
Updated: 2025-10-14T17:31:19+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1053
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
