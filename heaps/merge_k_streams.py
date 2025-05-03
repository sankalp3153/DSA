"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 478
Updated: 2025-05-03T22:13:15+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 478
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
