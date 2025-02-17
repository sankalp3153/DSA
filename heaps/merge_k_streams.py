"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 202
Updated: 2025-02-17T15:31:07+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 202
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
