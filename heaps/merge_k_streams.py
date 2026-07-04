"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 1927
Updated: 2026-07-04T18:28:09+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1927
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
