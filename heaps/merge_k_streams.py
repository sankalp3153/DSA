"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 1697
Updated: 2026-04-18T17:28:43+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1697
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
