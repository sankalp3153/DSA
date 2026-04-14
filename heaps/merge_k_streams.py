"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 1674
Updated: 2026-04-14T19:33:11+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1674
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
