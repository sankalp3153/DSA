"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 2019
Updated: 2026-07-31T14:16:57+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2019
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
