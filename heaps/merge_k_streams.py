"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 1651
Updated: 2026-04-09T11:41:31+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1651
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
