"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 1904
Updated: 2026-06-24T18:51:08+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 1904
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
