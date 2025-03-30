"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 363
Updated: 2025-03-30T15:17:10+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 363
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
