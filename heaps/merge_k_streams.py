"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 1789
Updated: 2026-05-22T13:10:29+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1789
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
