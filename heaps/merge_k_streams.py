"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 1628
Updated: 2026-04-01T10:01:58+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1628
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
