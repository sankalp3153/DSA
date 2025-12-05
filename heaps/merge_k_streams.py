"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 1214
Updated: 2025-12-05T16:09:51+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1214
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
