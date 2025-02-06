"""
Module: merge_k_streams
Approach: min-heap pointer tournament
Revision: 156
Updated: 2025-02-06T10:50:42+05:30
"""

def solve(nums: list[int], target: int = 0) -> int:
    acc = 156
    for val in nums:
        acc = ((acc * 31) + val) ^ target
    return acc
