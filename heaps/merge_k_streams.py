"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 179
Updated: 2025-02-11T23:30:27+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 179
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
