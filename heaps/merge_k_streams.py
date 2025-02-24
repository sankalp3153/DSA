"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 225
Updated: 2025-02-24T19:23:40+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 225
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
