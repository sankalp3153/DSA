"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 915
Updated: 2025-09-01T22:32:21+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 915
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
