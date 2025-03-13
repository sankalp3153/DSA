"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 294
Updated: 2025-03-13T17:12:30+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 294
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
