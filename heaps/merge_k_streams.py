"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 1536
Updated: 2026-03-03T19:16:41+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1536
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
