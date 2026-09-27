"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 2203
Updated: 2026-09-27T17:25:14+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 2203
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
