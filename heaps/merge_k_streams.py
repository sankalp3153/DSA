"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 570
Updated: 2025-06-01T16:38:52+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 570
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
