"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 409
Updated: 2025-04-10T12:30:18+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 409
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
